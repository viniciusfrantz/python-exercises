# Faça um Programa para um caixa eletrônico.
# O programa deverá perguntar ao usuário a valor
# do saque e depois informar quantas notas de cada
# valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50
# e 100 reais. O valor mínimo é de 10 reais e o
# máximo de 600 reais. O programa não deve se preocupar
# com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece
# duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa
# fornece três notas de 100,uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
while True:
    try:
        valor = int(input('Digite  o valor a ser sacado:'))
    except ValueError:
        print('Deve ser digitaso um valor inteiro:')
    else:
        if valor > 600:
            print('o valor máximo é de 600,00')
        else:
            notas_cem = notas_cinq = notas_dez = notas_cinco = notas_um = 0
            notas_cem, resto = divmod(valor, 100)
            notas_cinq, resto = divmod(resto, 50)
            notas_dez, resto = divmod(resto, 10)
            notas_cinco, resto = divmod(resto, 5)
            notas_um = resto
            if notas_cem > 0:
                print(f'{notas_cem} - nota(s) de 100')
            if notas_cinq > 0:
                print(f'{notas_cinq} - nota(s) de 50')
            if notas_dez > 0:
                print(f'{notas_dez} - nota(s) de 10')
            if notas_cinco > 0:
                print(f'{notas_cinco} - nota(s) de 5')
            if notas_um > 0:
                print(f'{notas_um} - nota(s) de 1')
            break

