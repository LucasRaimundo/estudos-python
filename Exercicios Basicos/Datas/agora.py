#!/usr/bin/env python3

__version__ = '0.1.0'
__author__ = 'LMR'

from datetime import date

now = date.today()
print(now.strftime("%d/%m/%Y"))