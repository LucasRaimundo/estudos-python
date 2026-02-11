#!/usr/bin/env python3

"""Carregue a data atual do computador e, com base na data atual, apresente a data de dois dias no futuro"""
__version__ = '0.1.0'
__author__ = 'LMR'

from datetime import date, timedelta

now = date.today()
futuro = now + timedelta(days=2)
print(now.strftime("%d/%m/%Y"), "/", futuro.strftime("%d/%m/%Y"))