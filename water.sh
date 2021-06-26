#!/bin/bash
if [[ ! $1 || $1 == "-h" ]]; then
    echo -e "Usage: $0 student_id"
    exit 1
fi
STUDENT_ID="$1"
json_out=$(curl --connect-timeout 5 --silent -H "Accept: application/json" -H "Content-type: application/json" -X POST -d "{\"stucode\": \"$STUDENT_ID\"}" "http://weixin.lrgj.net.cn/ics/rest/wxdev/getSurplusDegreeWaterMeter")
remaining=$(echo $json_out | jq -r '.data.surplusDeg')
if [[ -n "$remaining" && "$remaining" != null ]]; then
    echo -n $remaining
else
    echo -n NaN
fi
