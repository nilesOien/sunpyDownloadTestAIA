#!/usr/bin/env Rscript

tr <- read.table('testResults.txt', sep=',', header=F)

tm <- strptime(tr[,1], "%Y/%m/%d %H:%M:%S", tz="UTC")
status=tr[,2]

png('plot.png', height=600, width=1200)
plot(tm, status, col='red', pch=3,
     main='SDO download status vs UTC Time', xlab='UTC Time', ylab='Status (0=Good)',
     sub='Zero status indicates success')

q(save='no')

