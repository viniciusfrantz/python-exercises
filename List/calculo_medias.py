# Calcular média de aluno:
nota_1 = float(input('Digite a primeira nota:'))
nota_2 = float(input('Digite a segunda nota:'))
media = (nota_1 + nota_2)/2
if media >= 7:
    print(f'Aluno aprovado com nota: {media}')
elif 5 < media < 7:
    print(f'Aluno em exame com nota: {media}')
else:
    print(f'Aluno reprovado com nota: {media}')
