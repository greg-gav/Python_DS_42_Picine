#!/bin/sh
curl \
--data-urlencode "text=${1}" \
--data-urlencode "per_page=20" \
--data-urlencode "page=0" \
--get -k -H 'User-Agent: api-test-agent' 'https://api.hh.ru/vacancies' | jq "." > "hh.json"
