#!/bin/sh
cat ${1} | head -n 1 > hh_positions.csv
awk -F, '{var1 = "";var2 = "";var3 = "";}\
{if (tolower($3) ~ /junior/) {var1 = "Junior";}}\
{if (tolower($3) ~ /middle/) {var2 = "Middle";}}\
{if (tolower($3) ~ /senior/) {var3 = "Senior";}}\
{miss = "\"-\""; OFS=","}\
{if (length(var1) != 0 || length(var2) != 0 || length(var3) != 0)\
{$3 = "\"" var1 var2 var3 "\""; print $0;} else {$3 = miss; print $0}}\
' ${1} | tail -n +2 >> hh_positions.csv