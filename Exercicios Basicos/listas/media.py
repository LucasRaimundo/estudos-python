#!/usr/bin/env python3
"""Desenvolva um programa que armazene quatro notas em uma lista e que apresente: a média final, a maior nota e a menor nota"""

__version__="0.1.0"
__author__="LMR"

notas = []
soma = 0
for n in range(0,4):
    nota = int(input("Digite sua nota: "))
    notas.append(nota)

for nota in notas:
    soma += nota

media = soma / 4
print(f"A média é de: {media}, sua maior nota foi {max(notas)} e sua menor nota foi {min(notas)}")