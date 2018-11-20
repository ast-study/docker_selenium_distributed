#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import check_call


for counter in range(10):
    chrome_cmd = 'export BROWSER=chrome && python test_search.py'
    firefox_cmd = 'export BROWSER=firefox && python test_search.py'
    check_call(chrome_cmd, shell=True)
    check_call(firefox_cmd, shell=True)

# Execution time: about 18 minutes