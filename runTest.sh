#!/bin/bash

# Script that can be run by cron to test
# sunpy AIA downloads using pytest.
# Makes a note of the time if it fails.
# Currently run like this :
# 05,20,35,50 * * * * /home/noien/sunpyDownloadTestAIA/runTest.sh &> /home/noien/sunpyDownloadTestAIA/runTest.log

if [ ! -d "$HOME/sunpyDownloadTestAIA" ]
then
 exit 0
fi

cd $HOME/sunpyDownloadTestAIA
# Just so it finds uv
export PATH="$PATH":"$HOME"/.local/bin

uv run pytest
status="$?"
if [ "$status" -ne 0 ]
then
 date --utc +"%Y/%m/%d %H:%M:%S %Z" >> failureTimes.txt 
fi

exit 0

