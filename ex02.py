n1 = float(input('Digite a nota N1: '))
n2 = float(input('Digite a nota N2: '))

resultado = (n1 + n2) / 2

resultado2 = 'Aprovado e sem pendências' if resultado >= 6 else 'Reprovado!'
print(resultado2)