#! /usr/bin/env python2

# Developed by Olivia Lucca Fraser
# for Tenable Network Security

import sys
import argparse
import math

ATTRIBUTES = ["name", "total", "frequency", "average"]
COLOUR_ON = True
RAINBOW = ["yellow","green","blue","cyan","magenta","red"]

def colour(hue, shade="dark"):
    global COLOUR_ON
    if (not COLOUR_ON):
        return ""
    hues = {
        "reset":"0"
        ,"black":"30"
        ,"red":"31"
        ,"green":"32"
        ,"yellow":"33"
        ,"blue":"34"
        ,"magenta":"35"
        ,"cyan":"36"
    }
    shades = {
        "dark":"0"
        ,"light":"1"
    }
    return "\x1b["+shades[shade]+";"+hues[hue]+"m"

def rainbow(indent, light='light'):
    global RAINBOW
    l = len(RAINBOW)
    return colour(RAINBOW[indent % l],light)

def attribute_string ():
    global ATTRIBUTES
    s = "<"
    for attr in ATTRIBUTES:
        s += attr
        s += "|"
    s = s[:-1] + ">"
    return s

def step(row):
    call_or_ret=row.split(" ")[0]
    if (call_or_ret == "call"):
        return 1
    elif (call_or_ret == "ret"):
        return -1
    else:
        return 0

def frame_time(split_row):
    """Returns the tuple (frame_name, elapsed_time)"""
    timestamp = eval(split_row[0].split(",")[2].replace("]",""))
    row = split_row[1]
    frame_name = row.split(" ")[1].split("(")[0]
    if (frame_name == ""):
        frame_name = "INTERNAL"
    return (frame_name, timestamp)


def calc_timing_info(elapsed_frames):
    """Each frame is an tuple (frame_name, elapsed_time)"""
    times = {}
    for f in elapsed_frames:
        entry = ()
        fname = f[0]
        elapsed = f[1]
        if (f[0] in times):
            entry = ((times[fname])[0] + elapsed, (times[fname])[1] + 1)
        else:
            entry = (elapsed, 1)
        times[fname] = entry
    by_avg = []
    for fname in times.keys():
        avg = times[fname][0] / times[fname][1]
        by_avg.append((fname, times[fname][0], times[fname][1], avg))

    return by_avg


def display_timing_info (listing, sortby):
    global ATTRIBUTES
    stats = calc_timing_info(listing)
    idx = 3
    if (sortby in ATTRIBUTES):
        idx = ATTRIBUTES.index(sortby)
    print "\n-----------------------------------------------"
    print " _____ _       _             ___       __     "
    print "|_   _(_)_ __ (_)_ _  __ _  |_ _|_ _  / _|___ "
    print "  | | | | '  \| | ' \/ _` |  | || ' \|  _/ _ \ "
    print "  |_| |_|_|_|_|_|_||_\__, | |___|_||_|_| \___/ "
    print "                     |___/"
    print "-----------------------------------------------"
 
    for p in sorted(stats, key=(lambda e: e[idx])):
        print p[0] + (": {:f}s over {:d} call{:s},"+
                      " avg: {:f}s")\
                      .format(p[1],p[2],
                              ("" if p[2] == 1 else "s"),
                              p[3])
    return stats

def abridge_args (fnstring, abridge_len, s):
    fnstring = fnstring.strip()
    splitter = "(" if s == 1 else "->"
    splitat = 1
    if "call (internal)" in fnstring:
        splitter = ")("
    if splitter not in fnstring:
        return fnstring
    parts = fnstring.split(splitter, 1)
    if (len(parts[1]) <= abridge_len):
        return fnstring
    else:
        chunk = parts[1][:abridge_len]
        return parts[0] + splitter + chunk + \
            ("...)" if s == 1 else "...")

def prettify_trace (filename, depth=0, focus="MAIN",
                    show_origins=False, enum=False,
                    timing_info="", abridge=1024,
                    quiet=False):
    split_rows=[r.split("(TRACE) ")
                for r in open(filename).readlines()]
    indent=0
    n=0
    ret_from = ""
    ret_elapsed = 0
    elapsed_frames = []
    frame_stack = [("MAIN", frame_time(split_rows[0])[1])]
    fmt="{:"+str(int(math.ceil(math.log
         (len(split_rows), 10))))+"d}"
    for split_row in split_rows:
        s = step(split_row[1])
        action = abridge_args(split_row[1], abridge, s)
        ft = frame_time(split_row)
        n += 1
        if (s == 1): # 1 = call, -1 = ret, 0 = ?
            frame_stack.append(ft)
        elif (s == -1):
            try:
                r_ft = frame_stack.pop()
                ret_from = r_ft[0]
                ret_elapsed  = ft[1] - r_ft[1];
                elapsed_frames.append((ret_from,
                                       ret_elapsed))
            except:
                print >> sys.stderr, \
                    colour('red','light')+"<< call stack anomaly at line",n,">>"+ \
                    colour('reset')
                return
        ### Here's the noisy section:
        if ((not quiet) and (depth == 0 or depth > indent)
            and (focus in [ret_from]+[f[0] for f in frame_stack])):
            if (enum):
                print colour('black','light')+fmt.format(n)+colour('reset'),
            print rainbow(indent)+("  "*max(0,indent))+action+colour('reset'),
            if (s == -1):
                print rainbow(indent,'dark')+"[from {:s} after {:.8f}s]"\
                    .format(ret_from, ret_elapsed) + colour('reset')
                ret_from=""
            elif (show_origins and len(frame_stack) > 1):
                print rainbow(indent,'dark')+"[from {:s}]"\
                    .format(frame_stack[-2][0]) + colour('reset')
            else:
                print
        ### End of noisy section ###
        indent += s
    if (timing_info):
        display_timing_info(elapsed_frames, timing_info)



def main ():
    global COLOUR_ON
    parser = argparse.ArgumentParser(description =
                                     "Reconstruct call stack from nasl -T"+
                                     " trace, and structure trace output "+
                                     " accordingly.")
    parser.add_argument("tracefile", 
                        help="the output file generated by nasl -T")
    parser.add_argument("--depth", "-d", metavar="<calls deep>", type=int,
                        default=0,
                        help="how deep to peer into the call"+
                        " stack, in absolute terms")
    parser.add_argument("--function", "-f", metavar="<function name>",
                        type=str,
                        default="MAIN",
                        help="if you would like to restrict the"+
                        " view to just one function, name it")
    parser.add_argument("--sources", "-s", action="store_true", default=False,
                      help="display the name of the function from which each"+
                      " function is called")
    parser.add_argument("--timing", "-t", type=str, default="",
                        metavar=attribute_string(),
                        help="specify the attribute by which to sort the timing information")
    parser.add_argument("--enum", "-n", action="store_true", default=False,
                        help="enumerate the trace lines")
    parser.add_argument("--quiet", "-q", action="store_true", default=False)
    parser.add_argument("--abridge", "-a", type=int,
                        default=1024, help="abridge arguments longer "+
                        "than <n> characters", metavar="<n>")
    parser.add_argument("--rainbow", "-r", action="store_true", default=False,
                        help="colour-code the call stack")
    args = parser.parse_args()
    COLOUR_ON = args.rainbow
    prettify_trace(filename=args.tracefile,
                   depth=args.depth,
                   focus=args.function,
                   show_origins=args.sources,
                   enum=args.enum,
                   quiet=args.quiet,
                   abridge=args.abridge,
                   timing_info=args.timing)

if __name__ == "__main__":
    main()
