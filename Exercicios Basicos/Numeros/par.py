#!/usr/bin/env python3

"""Desenvolva um programa que leia um número inteiro qualquer e que informe se este número é par ou impar"""

__version__ = '0.1.0'
__author__ = 'LMR'

numero = int(input("Digite um número inteiro: "))

if numero % 2 ==0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")