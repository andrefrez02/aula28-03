media,freq = 0, 0.0

freq = int(input('Digite a frequência do aluno: '))
media = float(input('Digite a média do aluno: '))

if freq <= 75:
    print(f'{freq}% de frequência.\nO aluno foi reprovado por falta!')
elif media < 6.0: 
    print(f'{media} de média.\nO aluno foi reprovado por nota!')
else:
    print(f'{media} de média.\nO aluno foi aprovado por nota!')
