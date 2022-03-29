print(f'HOTEL CLEBAO\nTipos de diárias: \n"S" - Simples = R$255,50\n"D" - Duplo = R$305,50\n"T" - Triplo = R$360,50')
tipo = str(input('Digite o tipo de hospedagem que o sr. deseja: ("S" ou "D" ou "T"): '))

if tipo not in 'SsDdTt':
    print(f'Digite um valor válido para o tipo de hospedagem!!!')
else:
    qnt = int(input('Quantas noites o sr. ficará no hospedado?: '))
    if tipo in 'Ss':
        valor = 255.50 * qnt
    elif tipo in 'Dd':
        valor = 305.50 * qnt
    elif tipo in 'Tt':
        valor = 360.50 * qnt
    print(f'O valor da sua hospedagem ficará: R${valor:.2f}.')