#!/usr/bin/env python3

import sys

if len(sys.argv) > 2:
    for i in sys.argv[len(sys.argv) - 1: 0:-1]:
        print(i)
else:
    print('none')