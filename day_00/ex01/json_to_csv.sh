#!/bin/sh
jq -f --raw-output filter.jq ${1} > hh.csv