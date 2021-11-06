print('MÉDIA DOS ALUNOS ANO!')

a = float(input('DIGITE A NOTA DO PRIMEIRO BIMESTRE: '))
b = float(input('DIGITE A NOTA DO SEGUNDO BIMESTRE: '))
c = float(input('DIGITE A NOTA DO TERCEIRO BIMESTRE: '))
d = float(input('DIGITE A NOTA DO QUARTO BIMESTRE: '))

nota_final = (a + b + c + d) / 4

if (nota_final >= 6):
    print('Você foi aprovado! sua nota foi', nota_final)
else:
    print('Você foi reprovado! sua nota final foi', nota_final)
