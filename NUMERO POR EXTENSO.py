print('NÚMERO POR EXTENSO')
x = input('Digite um número: ')
dicionario_numerico = {
    'unidade': {
        'um': 1.,
        'dois': 2,
        'trêS': 3,
        'quatro': 4,
        'cinco': 5,
        'seis': 6,
        'sete': 7,
        'oito': 8,
        'nove': 9,
        'dez': 10
    },
    'onzeadezenove': {
        'onze': 11,
        'doze': 12,
        'treze': 13,
        'quatorze': 14,
        'quinze': 15,
        'dezeseis': 16,
        'dezesete': 17,
        'dezoito': 18,
        'dezenove': 19,

    },
    'vinteanoventa': {
        'vinte': 20,
        'trinta': 30,
        'quarenta': 40,
        'cinquenta': 50,
        'sessenta': 60,
        'setenta': 70,
        'oitenta': 80,
        'noventa': 90,

    },
    'cematenovecentos': {
        'cem': 100,
        'duzentos': 200,
        'trezentos': 300,
        'quatrocentos': 400,
        'quinhentos': 500,
        'seiscentos': 600,
        'setecentos': 700,
        'oitocentos': 800,
        'novecentos': 900,
    },

}

digitos = x
if x.isnumeric():
    x = len(x)


def UnidadeDezena():

    if x == 1:  # -verifica se o usuario digitou um unico numero
        for k, v in dicionario_numerico['unidade'].items():
            if int(digitos) == v:
                print('-'*10)
                print(k)
                print('-'*10)

    if x == 2 and digitos[0] == '1' and digitos[1] == '0':
        print('-'*10)
        print(k)
        print('-'*10)


if x == 2 and digitos[0]
