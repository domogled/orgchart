#!/usr/bin/env sh

COMMAND=pytest

# COMMAND="OrgChart/scripts/orgchart.py ./data/orgchart-data.csv ./data/employees-data.csv"

watchexec -c -w ./OrgChart -e py $COMMAND
