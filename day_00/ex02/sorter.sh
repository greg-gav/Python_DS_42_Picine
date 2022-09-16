#!/bin/sh
cat ${1} | head -n 1 > hh_sorted.csv
cat ${1} | tail -n +2 | sort -k2,2 -k1,1 -t, >> hh_sorted.csv