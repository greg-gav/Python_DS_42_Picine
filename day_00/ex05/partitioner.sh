#!/bin/sh
awk -F, '{if(NR==1) {header = $0; next}}
{split($2,a,"T"); var = a[1]; b[var]++;}{FS=","}
{if (b[var] == 1) print header > (substr(var, 2) "_date.csv");}
{print $0 >> (substr(var, 2) "_date.csv");}
' ${1}
