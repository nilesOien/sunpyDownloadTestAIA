#!/bin/bash

# Look at testResults.txt and calculate the percent good.

num=`cat testResults.txt | wc -l`
numBad=`cat testResults.txt | awk -F\, '{print $2}' | awk '{ sum += $1 } END { print sum }'`

pGood=`echo $num $numBad | awk '{print 100.0-100.0*$2/$1}'`

echo Precent good : $pGood with $numBad bad, $num total

