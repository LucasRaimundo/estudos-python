#!/usr/bin/env python3

"""Desenvolva um programa que leia um número inteiro qualquer e que apresete o número informado, seguido do seu antecessor e do seu sucessor
"""
__version__ = "0.1.0"
__author__ = "LMR"

num = int(input("Digite um número inteiro: "))
succ = num + 1
ant = num - 1
print("O numero informado foi: ", num, ", seu antecessor é: ", ant, " e seu sucessor é: ", succ)