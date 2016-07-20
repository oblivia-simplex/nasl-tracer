#! /bin/sh

echo "About to install to /usr/bin/trace"
echo "Hit <ENTER> to continue..."
read foo

if [ -f /usr/bin/trace ]; then
  echo "A file already exists at that location."
  echo "Hit <ENTER> to proceed, anyways, or <CTRL-C> to abort."
  read foo
fi
sudo cp trace.py /usr/bin/trace

