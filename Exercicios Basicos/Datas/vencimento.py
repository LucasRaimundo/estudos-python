#!/usr/bin/env python3

__version__ = '0.1.0'
__author__ = 'LMR'

from datetime import date, datetime

now = date.today()
data_usuario = input("Digite a data de vencimento (dd/mm/yyyy): ")

convertido = datetime.strptime(data_usuario, "%d/%m/%Y").date()


if convertido == now:
    print("A data de vencimento é hoje.")
elif convertido < now:
    diferenca = convertido - now
    print(f"A data de vencimento já passou há {diferenca.days} dias.")
else:
    diferenca = now - convertido
    print(f"A data de vencimento é daqui a {diferenca.days} dias.")

