#!/bin/sh
awk -F, '{if(NR==1) {header = $0; print $0 > "hh_concat.csv"; next}}
{if ($0 != header) print $0 >> "hh_concat.csv"}
' ${@}
cat hh_concat.csv| head -n 1 > hh_concat_sorted.csv
cat hh_concat.csv | tail -n +2 | sort -k2,2 -k1,1 -t, >> hh_concat_sorted.csv
rm hh_concat.csv