#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen


processes = []

for counter in range(10):
    chrome_cmd = 'export BROWSER=chrome && python test_search.py'
    firefox_cmd = 'export BROWSER=firefox && python test_search.py'
    processes.append(Popen(chrome_cmd, shell=True))
    processes.append(Popen(firefox_cmd, shell=True))

for counter in range(10):
    processes[counter].wait()

# Execution time: about 9 minutes