#!/usr/bin/env python3

"""Desenvolva um programa que leia quatro notas e que apresente a média final"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média final do aluno é de: {media:.2f}")