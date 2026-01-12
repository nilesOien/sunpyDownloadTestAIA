#!/usr/bin/env Rscript

tr <- read.table('testResults.txt', sep=',', header=F)

tm <- strptime(tr[,1], "%Y/%m/%d %H:%M:%S", tz="UTC")
tm <- strftime(tm, "%H")
status=tr[,2]

png('plot2.png', height=800, width=800)
# plot(tm, status, col='red', pch=3,
#      main='SDO download status vs UTC Hour', xlab='UTC Hour', ylab='Status (0=Good)',
#      sub='Zero status indicates success')

bad_indices <- which(status != 0) 

bad_hours <- sort(as.numeric(tm[bad_indices]))

bad_hours

hist(bad_hours, col='red', breaks=seq(from=-0.5, to=23.5, by=1.0),
     main='Histogram of SDO download fails by UTC Hour',
     xlab='UTC Hour', ylab='Number of failures')

q(save='no')

