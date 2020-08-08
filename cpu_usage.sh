#!/usr/bin/env bash

echo "`ps -A -o %cpu | awk '{s+=$1} END {print s "%"}'`"