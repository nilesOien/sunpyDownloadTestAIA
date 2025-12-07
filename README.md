# sunpyDownloadTestAIA

Small test suite that can be run in cron to test
the sunpy AIA downloads as documented at 
[this](https://docs.sunpy.org/en/latest/generated/gallery/map/track_active_region.html)
location.

Assuming you use uv, use the installSunpy.sh script to
install the required paython packages. You can then run
the tests by running runTest.sh in cron (there are comments
in that script that may be helpful).

Should a cron driven test fail, a note of the time
will be appended to the file failureTimes.txt


