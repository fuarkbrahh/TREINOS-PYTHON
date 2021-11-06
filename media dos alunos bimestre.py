print('MÉDIA DOS ALUNOS!')

a = (float(input('DIGITE A SUA PRIMEIRA NOTA: ')))
b = (float(input('DIGITE A SUA SEGUNDA NOTA: ')))
c = (a + b) / 2

if (c >= 6):
    print('Você foi aprovado" sua nota é', c)
else:
    print('Você foi reprovado! sua nota é', c)
