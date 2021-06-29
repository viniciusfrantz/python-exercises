# Programa para decompor numero em centenas, dezenas e unidades
numero = int(input('Digite um número entre 0 e 1000:'))

centena_str = dezena_str = unidade_str = ''
centena, resto = divmod(numero, 100)

if centena == 1:
    centena_str = '1 centena'
elif centena > 1:
    centena_str = f'{centena} centenas'

dezena, unidade = divmod(resto, 10)

if dezena == 1:
    dezena_str = '1 dezena'
elif dezena > 1:
    dezena_str = f'{dezena} dezenas'

if unidade == 1:
    unidade_str = '1 unidade'
elif unidade > 1:
    unidade_str = f'{unidade} unidades'

if centena_str != '' and dezena_str != '' and unidade_str != '':
    print(f'{centena_str}, {dezena_str} e {unidade_str}')
elif centena_str != '' and dezena_str != '' and unidade_str == '':
    print(f'{centena_str} e {dezena_str}')
elif centena_str == '' and dezena_str != '' and unidade_str != '':
    print(f'{dezena_str} e {unidade_str}')
else:
    print(f'{centena_str}{dezena_str} {unidade_str}')
