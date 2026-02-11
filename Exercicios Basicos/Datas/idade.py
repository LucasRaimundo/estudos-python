#!/usr/bin/env python3

__version__="0.1.0"
__author__="LMR"


from datetime import date, datetime
from dateutil.relativedelta import relativedelta

now = date.today()

data_nascimento = input('Digite o ano que você nasceu em dd/mm/yyyy: ')
convertido = datetime.strptime(data_nascimento,"%d/%m/%Y").date()

anos = relativedelta(now,convertido)

print(anos)