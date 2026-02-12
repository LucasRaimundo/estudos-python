#!/usr/bin/env python3

"""Desenvolva um programa que armazene quatro notas em uma lista e que apresente a média final. Caso a média seja igual ou superior a 7, apresentar a mensagem "APROVADO", caso contrário, armazenar a nota da prova final e recalcular a média. Caso a nova média seja igual superior a 5, apresentar a mensagem "APROVADO", caso contrário, apresentar a mensagem REPROVADO"""

__author__="LMR"
__version="0.1.0"

notas = []
soma = 0
media = 0
for n in range(0,4):
    nota = int(input("Digite sua nota: "))
    notas.append(nota)

for nota in notas:
    soma += nota

media = soma / 4

if media >= 7:
    print("Aprovado!")
else:
    prova_final = int(input("Digite a nota final da sua prova: "))
    notas.append(prova_final)
    soma += prova_final
    media = soma / 5
    if media >= 5:
        print("Aprovado")
    else:
        print("Reprovado")