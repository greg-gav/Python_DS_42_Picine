#!/bin/sh
echo "\"name\",\"count\"" > hh_uniq_positions.csv
awk -F, '{if (tolower($3) ~ /junior/) {var1++;}}
{if (tolower($3) ~ /middle/) {var2++;}}
{if (tolower($3) ~ /senior/) {var3++;}}
END {
    {if (var1 != 0) print "\"Junior\"," var1;}
    {if (var2 != 0) print "\"Middle\"," var2;}
    {if (var3 != 0) print "\"Senior\"," var3;}
}
' ${1} | sort -k2,2 -rn -t, >> hh_uniq_positions.csv
