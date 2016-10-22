#!/usr/bin/python
# -*- coding: utf-8 -*-

largest = None

for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest :
        largest = itervar

print('Largest:', largest)