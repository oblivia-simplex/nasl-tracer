|>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<|
                 _   _                           
 _ __   __ _ ___| | | |_ _ __ __ _  ___ ___ _ __ 
| '_ \ / _` / __| | | __| '__/ _` |/ __/ _ \ '__|
| | | | (_| \__ \ | | |_| | | (_| | (_|  __/ |   
|_| |_|\__,_|___/_|  \__|_|  \__,_|\___\___|_|   
                                                 

A tool for parsing the output of nasl -T, reconstructing the
call stack, and reformatting the trace in a way that makes it
much more meaningful and useful to you, the debugger.

|>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<|
                         _
 _____ ____ _ _ __  _ __| |___
/ -_) \ / _` | '  \| '_ \ / -_)
\___/_\_\__,_|_|_|_| .__/_\___|
                   |_|

nasl -T will generate an output file that looks something like this:

|>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<|

[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549399] (TRACE) call get_kb_item(global_settings/supplied_logins_only )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549474] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549479] (TRACE) call get_kb_item(global_settings/network_type )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549481] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549483] (TRACE) call get_kb_item(global_settings/report_verbosity )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549485] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549487] (TRACE) call get_kb_item(global_settings/report_paranoia )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549489] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549490] (TRACE) call get_kb_item(global_settings/debug_level )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549492] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549494] (TRACE) call int()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549496] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549498] (TRACE) call get_kb_item(global_settings/experimental_scripts )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549500] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549502] (TRACE) call get_kb_item(global_settings/thorough_tests )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549504] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549507] (TRACE) call make_list(1 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549517] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549522] (TRACE) call (internal)(.91)!....:2*"....;3+#....<4,$?7/'....>6.&....=5-%........ )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549529] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549531] (TRACE) call (internal)(.........................)4.%/7.(3-!0,1'8"5.*2$.  )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549536] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549538] (TRACE) call (internal)(.:2*"....<4,$....>6.&....@80( ...91)!....;3+#....=5-%....?7/'.... )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549544] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549546] (TRACE) call (internal)(. ............................................. . )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549551] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549553] (TRACE) call (internal)(..................... ........... )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549557] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549558] (TRACE) call (internal)(.(.0.8.@ './.7.?.&...6.>.%.-.5.=.$.,.4.<.#.+.3.;.".*.2.:.!.).1.9. )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549564] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549566] (TRACE) call (internal)(................. )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549569] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549570] (TRACE) call (internal)(................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................. )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549606] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549608] (TRACE) call (internal)(................................................. )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549613] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549615] (TRACE) call (internal)(................................................. )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549684] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549686] (TRACE) call (internal)(......................................................... )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549691] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549693] (TRACE) call (internal)(......................................... )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549697] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549699] (TRACE) call (internal)(......................................... )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549703] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549704] (TRACE) call (internal)(......................................... )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549709] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549710] (TRACE) call (internal)(......................................... )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549715] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549716] (TRACE) call (internal)(......................................... )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549721] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549722] (TRACE) call (internal)(................................................................. )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549728] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549730] (TRACE) call (internal)(................................................................. )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549736] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549738] (TRACE) call make_list(Sun , Mon , Tue , Wed , Thu , Fri , Sat , Sun )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549742] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549745] (TRACE) call make_list( , Jan , Feb , Mar , Apr , May , Jun , Jul , Aug , Sep , Oct , Nov , Dec )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549750] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549755] (TRACE) call make_list()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549757] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549758] (TRACE) call make_list()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549760] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549762] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549769] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549771] (TRACE) call make_list(1 , %s(): Unknown or upstream error occurred. , -1 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549775] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549777] (TRACE) call make_list(2 , %s(): missing required argument '%s'. , -2 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549781] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549782] (TRACE) call make_list(3 , %s(): '%s' arg must be type '%s'. , -3 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549785] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549786] (TRACE) call make_list(2 , %s(): '%s' variable is unexpectedly NULL. , -4 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549789] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549791] (TRACE) call make_list(2 , %s(): Failure parsing variable '%s'. , -5 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549794] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549795] (TRACE) call make_list(3 , %s(): The function '%s' is not defined. Try including '%s'. , -6 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549798] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549800] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549813] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549815] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549816] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549819] (TRACE) call get_http_port(, 8081 , , , , , , )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549823] (TRACE) call get_kb_item(Services/www )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549825] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549828] (TRACE) call get_port_state(8081 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549837] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549845] (TRACE) call get_kb_item(Services/www/8081/embedded )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549848] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549851] (TRACE) call http_is_broken(, 8081 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549855] (TRACE) call get_kb_item(Services/www/8081/broken )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549857] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549860] (TRACE) call get_kb_item(Services/www/8081/working )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549862] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549864] (TRACE) call get_read_timeout()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549867] (TRACE) call get_preference(checks_read_timeout )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549875] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549877] (TRACE) call int()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549878] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549880] (TRACE) ret -> 5 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549882] (TRACE) call unixtime()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549887] (TRACE) ret -> 1467992266 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549891] (TRACE) call http_send_recv3(, , , , , , , / , GET , 1 , , , 8081 , , , , 11 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549895] (TRACE) call strlen(/ )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549896] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549900] (TRACE) call http_mk_req(, , , , / , GET , 8081 , 11 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549903] (TRACE) call isnull(8081 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549905] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549907] (TRACE) call isnull(GET )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549908] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549911] (TRACE) call strlen(/ )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549912] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549914] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549915] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549917] (TRACE) call init_cookiejar()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549918] (TRACE) call clear_cookiejar()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549919] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549921] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549922] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549924] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549925] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549926] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549927] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549929] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549930] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549931] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549932] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549950] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549952] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549953] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549954] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549956] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549957] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549959] (TRACE) call load_cookiejar(FormAuth )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549961] (TRACE) call isnull(FormAuth )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549963] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549966] (TRACE) call get_kb_list(Cookies/FormAuth/value/* )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549971] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549972] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549973] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549976] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549977] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549979] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549980] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549981] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549983] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549985] (TRACE) call isnull(11 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549986] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549988] (TRACE) call int(11 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549989] (TRACE) ret -> 11 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549992] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549993] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549996] (TRACE) call get_kb_item(www/8081/http11_hostname )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.549999] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550000] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550001] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550004] (TRACE) call get_host_ip()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550007] (TRACE) ret -> 127.0.0.1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550010] (TRACE) call get_preference(sc.hostname.127.0.0.1 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550012] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550014] (TRACE) call strlen()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550015] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550017] (TRACE) call get_host_name()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550019] (TRACE) ret -> localhost 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550020] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550022] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550032] (TRACE) call strcat(GET ,   , / ,  HTTP/1.1 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550035] (TRACE) ret -> GET / HTTP/1.1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550038] (TRACE) call get_kb_item(global_settings/http_user_agent )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550041] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550053] (TRACE) call mk_cookie_header(/ )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550056] (TRACE) call isnull(<array> )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550057] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550059] (TRACE) call keys(<array> )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550061] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550063] (TRACE) call sort()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550072] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550074] (TRACE) call max_index()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550075] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550078] (TRACE) call strlen( )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550079] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550081] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550085] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550087] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550089] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550090] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550092] (TRACE) call typeof()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550098] (TRACE) ret -> undef 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550101] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550104] (TRACE) call isnull(<array> )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550105] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550108] (TRACE) call http_send_recv_req(, , , 1 , , , 8081 , <array> , , , )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550112] (TRACE) call http_keepalive_enabled(, 8081 , , )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550115] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550116] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550118] (TRACE) call get_host_ip()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550121] (TRACE) ret -> 127.0.0.1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550123] (TRACE) call get_preference(sc.hostname.127.0.0.1 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550125] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550126] (TRACE) call strlen()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550128] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550129] (TRACE) call get_host_name()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550131] (TRACE) ret -> localhost 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550133] (TRACE) call http_mk_get_req(, , localhost , / , 8081 , 11 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550137] (TRACE) call http_mk_req(, , , localhost , / , GET , 8081 , 11 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550140] (TRACE) call isnull(8081 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550142] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550143] (TRACE) call isnull(GET )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550144] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550147] (TRACE) call strlen(/ )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550148] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550149] (TRACE) call isnull(<array> )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550151] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550152] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550153] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550155] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550156] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550158] (TRACE) call isnull(11 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550159] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550161] (TRACE) call int(11 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550162] (TRACE) ret -> 11 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550164] (TRACE) call isnull(localhost )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550166] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550167] (TRACE) call make_array()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550169] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550175] (TRACE) call strcat(GET ,   , / ,  HTTP/1.1 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550186] (TRACE) ret -> GET / HTTP/1.1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550189] (TRACE) call get_kb_item(global_settings/http_user_agent )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550191] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550201] (TRACE) call mk_cookie_header(/ )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550204] (TRACE) call isnull(<array> )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550205] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550207] (TRACE) call keys(<array> )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550208] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550210] (TRACE) call sort()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550211] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550212] (TRACE) call max_index()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550214] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550216] (TRACE) call strlen( )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550217] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550219] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550223] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550224] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550226] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550227] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550229] (TRACE) call typeof()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550230] (TRACE) ret -> undef 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550233] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550234] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550244] (TRACE) call http_open_sock_err(8081 , , )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550246] (TRACE) call gettimeofday()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550254] (TRACE) ret -> 1467992266.550251 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550257] (TRACE) call open_sock_tcp(, , , , 8081 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550388] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550394] (TRACE) call gettimeofday()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550398] (TRACE) ret -> 1467992266.550395 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550401] (TRACE) call split(0 , . , 1467992266.550395 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550407] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550411] (TRACE) call int(1467992266 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550414] (TRACE) ret -> 1467992266 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550417] (TRACE) call http_get_read_timeout()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550419] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550420] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550422] (TRACE) call get_read_timeout()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550423] (TRACE) call get_preference(checks_read_timeout )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550426] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550427] (TRACE) call int()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550429] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550431] (TRACE) ret -> 5 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550432] (TRACE) ret -> 5 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550434] (TRACE) call difftime(1467992266.550251 , 1467992266.550395 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550437] (TRACE) call split(0 , . , 1467992266.550251 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550441] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550443] (TRACE) call int(1467992266 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550460] (TRACE) ret -> 1467992266 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550463] (TRACE) call int(550251 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550464] (TRACE) ret -> 550251 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550466] (TRACE) call split(0 , . , 1467992266.550395 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550470] (TRACE) ret -> <array> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550473] (TRACE) call int(1467992266 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550475] (TRACE) ret -> 1467992266 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550477] (TRACE) call int(550395 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550478] (TRACE) ret -> 550395 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550482] (TRACE) ret -> 144 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550486] (TRACE) call defined_func(socket_get_error )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550509] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550512] (TRACE) call debug_print(, , , , , , , , , , , http_open_sock_err: connection to TCP port  , 8081 ,  failed - errno= , 6 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550523] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550524] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550527] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550530] (TRACE) call http_set_error(6 , , connecting to server , 8081 , , )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550534] (TRACE) call isnull(8081 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550535] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550537] (TRACE) call isnull(6 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550538] (TRACE) ret -> 0 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550540] (TRACE) call http_strerror(6 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550544] (TRACE) call int(6 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550546] (TRACE) ret -> 6 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550549] (TRACE) ret -> connection refused 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550552] (TRACE) call debug_print(, , , , , , , , , , , http_set_error: port= , 8081 ,  errno= , 6 ,  ( , connection refused , ), op= , connecting to server , . )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550563] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550564] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550566] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550569] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550571] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550572] (TRACE) call unixtime()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550574] (TRACE) ret -> 1467992266 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550578] (TRACE) call get_kb_item(www/8081/unresponsive/time )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550580] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550584] (TRACE) call get_kb_item(www/8081/unresponsive/nb )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550586] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550589] (TRACE) call replace_kb_item(www/8081/unresponsive/nb , 1 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550595] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550598] (TRACE) call replace_kb_item(www/8081/unresponsive/time , 1467992266 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550602] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550604] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550606] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550610] (TRACE) ret -> -2 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550616] (TRACE) call debug_print(, , , , , , , , , , , http_send_recv_req(port:  , 8081 , ): http_keepalive_enabled failed. )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550635] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550637] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550639] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550641] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550643] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550644] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550648] (TRACE) call debug_print(, , , , , , , , , , , http_send_recv3(port:  , 8081 , , host:  , , , transport:  , , , method:  , GET , , item:  , / , , data= , , , version:  , 11 , , follow_redirect:  , , ): http_send_recv_req failed. )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550665] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550666] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550668] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550671] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550676] (TRACE) call isnull()
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550677] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550679] (TRACE) call declare_broken_web_server(8081 , The web server failed to respond. )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550683] (TRACE) call replace_kb_item(Services/www/8081/broken , 1 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550688] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550689] (TRACE) call defined_func(rm_kb_item )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550698] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550702] (TRACE) call rm_kb_item(Services/www/8081/working , 1 )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550705] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550708] (TRACE) call replace_kb_item(Services/www/8081/declared_broken_by , sonatype_nexus_detect.nasl )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550713] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550717] (TRACE) call replace_kb_item(Services/www/8081/broken/reason , The web server failed to respond. )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550722] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550723] (TRACE) ret -> 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550725] (TRACE) ret -> 1 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550728] (TRACE) call strcat(The web server on port  , 8081 ,  is broken. )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550732] (TRACE) ret -> The web server on port 8081 is broken. 
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550734] (TRACE) call exit(1 , The web server on port 8081 is broken. )
[sonatype_nexus_detect.nasl, 10809.3, 1467992266.550822] (TRACE) ret -> 

|>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<|

Which is a mess, and time-consuming to read and makes sense of.

But pass this to trace.py, and you get something somewhat more useful:

|>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<|

call get_kb_item(global_settings/supplied_logins_only )
  ret ->  from get_kb_item
call get_kb_item(global_settings/network_type )
  ret ->  from get_kb_item
call get_kb_item(global_settings/report_verbosity )
  ret ->  from get_kb_item
call get_kb_item(global_settings/report_paranoia )
  ret ->  from get_kb_item
call get_kb_item(global_settings/debug_level )
  ret ->  from get_kb_item
call int()
  ret -> 0  from int
call get_kb_item(global_settings/experimental_scripts )
  ret ->  from get_kb_item
call get_kb_item(global_settings/thorough_tests )
  ret ->  from get_kb_item
call make_list(1 )
  ret -> <array>  from make_list
call (internal)(.91)!....:2*"....;3+#....<4,$?7/'....>6.&....=5-%........ )
  ret -> <array>  from 
call (internal)(.........................)4.%/7.(3-!0,1'8"5.*2$.  )
  ret -> <array>  from 
call (internal)(.:2*"....<4,$....>6.&....@80( ...91)!....;3+#....=5-%....?7/'.... )
  ret -> <array>  from 
call (internal)(. ............................................. . )
  ret -> <array>  from 
call (internal)(..................... ........... )
  ret -> <array>  from 
call (internal)(.(.0.8.@ './.7.?.&...6.>.%.-.5.=.$.,.4.<.#.+.3.;.".*.2.:.!.).1.9. )
  ret -> <array>  from 
call (internal)(................. )
  ret -> <array>  from 
call (internal)(................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................. )
  ret -> <array>  from 
call (internal)(................................................. )
  ret -> <array>  from 
call (internal)(................................................. )
  ret -> <array>  from 
call (internal)(......................................................... )
  ret -> <array>  from 
call (internal)(......................................... )
  ret -> <array>  from 
call (internal)(......................................... )
  ret -> <array>  from 
call (internal)(......................................... )
  ret -> <array>  from 
call (internal)(......................................... )
  ret -> <array>  from 
call (internal)(......................................... )
  ret -> <array>  from 
call (internal)(................................................................. )
  ret -> <array>  from 
call (internal)(................................................................. )
  ret -> <array>  from 
call make_list(Sun , Mon , Tue , Wed , Thu , Fri , Sat , Sun )
  ret -> <array>  from make_list
call make_list( , Jan , Feb , Mar , Apr , May , Jun , Jul , Aug , Sep , Oct , Nov , Dec )
  ret -> <array>  from make_list
call make_list()
  ret -> <array>  from make_list
call make_list()
  ret -> <array>  from make_list
call make_array()
  ret -> <array>  from make_array
call make_list(1 , %s(): Unknown or upstream error occurred. , -1 )
  ret -> <array>  from make_list
call make_list(2 , %s(): missing required argument '%s'. , -2 )
  ret -> <array>  from make_list
call make_list(3 , %s(): '%s' arg must be type '%s'. , -3 )
  ret -> <array>  from make_list
call make_list(2 , %s(): '%s' variable is unexpectedly NULL. , -4 )
  ret -> <array>  from make_list
call make_list(2 , %s(): Failure parsing variable '%s'. , -5 )
  ret -> <array>  from make_list
call make_list(3 , %s(): The function '%s' is not defined. Try including '%s'. , -6 )
  ret -> <array>  from make_list
call make_array()
  ret -> <array>  from make_array
call make_array()
  ret -> <array>  from make_array
call get_http_port(, 8081 , , , , , , )
  call get_kb_item(Services/www )
    ret ->  from get_kb_item
  call get_port_state(8081 )
    ret -> 1  from get_port_state
  call get_kb_item(Services/www/8081/embedded )
    ret ->  from get_kb_item
  call http_is_broken(, 8081 )
    call get_kb_item(Services/www/8081/broken )
      ret ->  from get_kb_item
    call get_kb_item(Services/www/8081/working )
      ret ->  from get_kb_item
    call get_read_timeout()
      call get_preference(checks_read_timeout )
        ret ->  from get_preference
      call int()
        ret -> 0  from int
      ret -> 5  from get_read_timeout
    call unixtime()
      ret -> 1467992266  from unixtime
    call http_send_recv3(, , , , , , , / , GET , 1 , , , 8081 , , , , 11 )
      call strlen(/ )
        ret -> 1  from strlen
      call http_mk_req(, , , , / , GET , 8081 , 11 )
        call isnull(8081 )
          ret -> 0  from isnull
        call isnull(GET )
          ret -> 0  from isnull
        call strlen(/ )
          ret -> 1  from strlen
        call isnull()
          ret -> 1  from isnull
        call init_cookiejar()
          call clear_cookiejar()
            call make_array()
              ret -> <array>  from make_array
            call make_array()
              ret -> <array>  from make_array
            call make_array()
              ret -> <array>  from make_array
            call make_array()
              ret -> <array>  from make_array
            call make_array()
              ret -> <array>  from make_array
            call make_array()
              ret -> <array>  from make_array
            call make_array()
              ret -> <array>  from make_array
            call make_array()
              ret -> <array>  from make_array
            ret ->  from clear_cookiejar
          call load_cookiejar(FormAuth )
            call isnull(FormAuth )
              ret -> 0  from isnull
            call get_kb_list(Cookies/FormAuth/value/* )
              ret ->  from get_kb_list
            call isnull()
              ret -> 1  from isnull
            ret -> 1  from load_cookiejar
          ret ->  from init_cookiejar
        call isnull()
          ret -> 1  from isnull
        call make_array()
          ret -> <array>  from make_array
        call isnull(11 )
          ret -> 0  from isnull
        call int(11 )
          ret -> 11  from int
        call isnull()
          ret -> 1  from isnull
        call get_kb_item(www/8081/http11_hostname )
          ret ->  from get_kb_item
        call isnull()
          ret -> 1  from isnull
        call get_host_ip()
          ret -> 127.0.0.1  from get_host_ip
        call get_preference(sc.hostname.127.0.0.1 )
          ret ->  from get_preference
        call strlen()
          ret -> 0  from strlen
        call get_host_name()
          ret -> localhost  from get_host_name
        call make_array()
          ret -> <array>  from make_array
        call strcat(GET ,   , / ,  HTTP/1.1 )
          ret -> GET / HTTP/1.1  from strcat
        call get_kb_item(global_settings/http_user_agent )
          ret ->  from get_kb_item
        call mk_cookie_header(/ )
          call isnull(<array> )
            ret -> 0  from isnull
          call keys(<array> )
            ret ->  from keys
          call sort()
            ret ->  from sort
          call max_index()
            ret ->  from max_index
          call strlen( )
            ret -> 0  from strlen
          ret ->  from mk_cookie_header
        call isnull()
          ret -> 1  from isnull
        call isnull()
          ret -> 1  from isnull
        call typeof()
          ret -> undef  from typeof
        ret -> <array>  from http_mk_req
      call isnull(<array> )
        ret -> 0  from isnull
      call http_send_recv_req(, , , 1 , , , 8081 , <array> , , , )
        call http_keepalive_enabled(, 8081 , , )
          call isnull()
            ret -> 1  from isnull
          call get_host_ip()
            ret -> 127.0.0.1  from get_host_ip
          call get_preference(sc.hostname.127.0.0.1 )
            ret ->  from get_preference
          call strlen()
            ret -> 0  from strlen
          call get_host_name()
            ret -> localhost  from get_host_name
          call http_mk_get_req(, , localhost , / , 8081 , 11 )
            call http_mk_req(, , , localhost , / , GET , 8081 , 11 )
              call isnull(8081 )
                ret -> 0  from isnull
              call isnull(GET )
                ret -> 0  from isnull
              call strlen(/ )
                ret -> 1  from strlen
              call isnull(<array> )
                ret -> 0  from isnull
              call isnull()
                ret -> 1  from isnull
              call make_array()
                ret -> <array>  from make_array
              call isnull(11 )
                ret -> 0  from isnull
              call int(11 )
                ret -> 11  from int
              call isnull(localhost )
                ret -> 0  from isnull
              call make_array()
                ret -> <array>  from make_array
              call strcat(GET ,   , / ,  HTTP/1.1 )
                ret -> GET / HTTP/1.1  from strcat
              call get_kb_item(global_settings/http_user_agent )
                ret ->  from get_kb_item
              call mk_cookie_header(/ )
                call isnull(<array> )
                  ret -> 0  from isnull
                call keys(<array> )
                  ret ->  from keys
                call sort()
                  ret ->  from sort
                call max_index()
                  ret ->  from max_index
                call strlen( )
                  ret -> 0  from strlen
                ret ->  from mk_cookie_header
              call isnull()
                ret -> 1  from isnull
              call isnull()
                ret -> 1  from isnull
              call typeof()
                ret -> undef  from typeof
              ret -> <array>  from http_mk_req
            ret -> <array>  from http_mk_get_req
          call http_open_sock_err(8081 , , )
            call gettimeofday()
              ret -> 1467992266.550251  from gettimeofday
            call open_sock_tcp(, , , , 8081 )
              ret -> 0  from open_sock_tcp
            call gettimeofday()
              ret -> 1467992266.550395  from gettimeofday
            call split(0 , . , 1467992266.550395 )
              ret -> <array>  from split
            call int(1467992266 )
              ret -> 1467992266  from int
            call http_get_read_timeout()
              call isnull()
                ret -> 1  from isnull
              call get_read_timeout()
                call get_preference(checks_read_timeout )
                  ret ->  from get_preference
                call int()
                  ret -> 0  from int
                ret -> 5  from get_read_timeout
              ret -> 5  from http_get_read_timeout
            call difftime(1467992266.550251 , 1467992266.550395 )
              call split(0 , . , 1467992266.550251 )
                ret -> <array>  from split
              call int(1467992266 )
                ret -> 1467992266  from int
              call int(550251 )
                ret -> 550251  from int
              call split(0 , . , 1467992266.550395 )
                ret -> <array>  from split
              call int(1467992266 )
                ret -> 1467992266  from int
              call int(550395 )
                ret -> 550395  from int
              ret -> 144  from difftime
            call defined_func(socket_get_error )
              ret -> 1  from defined_func
            call debug_print(, , , , , , , , , , , http_open_sock_err: connection to TCP port  , 8081 ,  failed - errno= , 6 )
              call isnull()
                ret -> 1  from isnull
              ret -> 1  from debug_print
            call http_set_error(6 , , connecting to server , 8081 , , )
              call isnull(8081 )
                ret -> 0  from isnull
              call isnull(6 )
                ret -> 0  from isnull
              call http_strerror(6 )
                call int(6 )
                  ret -> 6  from int
                ret -> connection refused  from http_strerror
              call debug_print(, , , , , , , , , , , http_set_error: port= , 8081 ,  errno= , 6 ,  ( , connection refused , ), op= , connecting to server , . )
                call isnull()
                  ret -> 1  from isnull
                ret -> 1  from debug_print
              call isnull()
                ret -> 1  from isnull
              call unixtime()
                ret -> 1467992266  from unixtime
              call get_kb_item(www/8081/unresponsive/time )
                ret ->  from get_kb_item
              call get_kb_item(www/8081/unresponsive/nb )
                ret ->  from get_kb_item
              call replace_kb_item(www/8081/unresponsive/nb , 1 )
                ret ->  from replace_kb_item
              call replace_kb_item(www/8081/unresponsive/time , 1467992266 )
                ret ->  from replace_kb_item
              ret ->  from http_set_error
            ret ->  from http_open_sock_err
          ret -> -2  from http_keepalive_enabled
        call debug_print(, , , , , , , , , , , http_send_recv_req(port:  , 8081 , ): http_keepalive_enabled failed. )
          call isnull()
            ret -> 1  from isnull
          ret -> 1  from debug_print
        ret ->  from http_send_recv_req
      call isnull()
        ret -> 1  from isnull
      call debug_print(, , , , , , , , , , , http_send_recv3(port:  , 8081 , , host:  , , , transport:  , , , method:  , GET , , item:  , / , , data= , , , version:  , 11 , , follow_redirect:  , , ): http_send_recv_req failed. )
        call isnull()
          ret -> 1  from isnull
        ret -> 1  from debug_print
      ret ->  from http_send_recv3
    call isnull()
      ret -> 1  from isnull
    call declare_broken_web_server(8081 , The web server failed to respond. )
      call replace_kb_item(Services/www/8081/broken , 1 )
        ret ->  from replace_kb_item
      call defined_func(rm_kb_item )
        ret -> 1  from defined_func
      call rm_kb_item(Services/www/8081/working , 1 )
        ret ->  from rm_kb_item
      call replace_kb_item(Services/www/8081/declared_broken_by , sonatype_nexus_detect.nasl )
        ret ->  from replace_kb_item
      call replace_kb_item(Services/www/8081/broken/reason , The web server failed to respond. )
        ret ->  from replace_kb_item
      ret ->  from declare_broken_web_server
    ret -> 1  from http_is_broken
  call strcat(The web server on port  , 8081 ,  is broken. )
    ret -> The web server on port 8081 is broken.  from strcat
  call exit(1 , The web server on port 8081 is broken. )
    ret ->  from exit

|>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<|

Or, suppose you just want to zero in on one function, and restrict the
detail to a depth of no greater than 3 call. Run

./trace.py tracefile.txt -d 3 -f http_is_broken

and you get:

|>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<|

call http_is_broken(, 8081 )
    call get_kb_item(Services/www/8081/broken )
      ret ->  from get_kb_item
    call get_kb_item(Services/www/8081/working )
      ret ->  from get_kb_item
    call get_read_timeout()
      call get_preference(checks_read_timeout )
      call int()
      ret -> 5  from get_read_timeout
    call unixtime()
      ret -> 1467992266  from unixtime
    call http_send_recv3(, , , , , , , / , GET , 1 , , , 8081 , , , , 11 )
      call strlen(/ )
      call http_mk_req(, , , , / , GET , 8081 , 11 )
      call isnull(<array> )
      call http_send_recv_req(, , , 1 , , , 8081 , <array> , , , )
      call isnull()
      call debug_print(, , , , , , , , , , , http_send_recv3(port:  , 8081 , , host:  , , , transport:  , , , method:  , GET , , item:  , / , , data= , , , version:  , 11 , , follow_redirect:  , , ): http_send_recv_req failed. )
      ret ->  from http_send_recv3
    call isnull()
      ret -> 1  from isnull
    call declare_broken_web_server(8081 , The web server failed to respond. )
      call replace_kb_item(Services/www/8081/broken , 1 )
      call defined_func(rm_kb_item )
      call rm_kb_item(Services/www/8081/working , 1 )
      call replace_kb_item(Services/www/8081/declared_broken_by , sonatype_nexus_detect.nasl )
      call replace_kb_item(Services/www/8081/broken/reason , The web server failed to respond. )
      ret ->  from declare_broken_web_server
    ret -> 1  from http_is_broken
