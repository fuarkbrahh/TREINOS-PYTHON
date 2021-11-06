from datetime import datetime
from typing import MutableSequence

meu_aniversario = (input('digite a data de seu próximo aniversário: '))

date = datetime(day=int(meu_aniversario[0:2]),
                month=int(meu_aniversario[2:4]),
                year=int(meu_aniversario[4:8]))

print(date)

dias_para_aniversário = date - datetime.now()

print(dias_para_aniversário)
