# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista, depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o programa. No final mostre:
   # Quantas pessoas foram cadastradas
   # Mostre o maior peso
   # Mostre o menor peso


temp = list()
dados = list()
maiorpeso = menorpeso = 0

while True: 
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ').replace(',', '.')))

    if len(dados) == 0:
        maiorpeso = menorpeso = temp[1]
    else: 
        if temp[1] > maiorpeso:
            maiorpeso = temp[1]
        if temp[1] < menorpeso:
            menorpeso = temp[1]
    dados.append(temp[:])
    temp.clear()

    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break

print(f'Você cadastrou {len(dados)} pessoa(s)')
print(f'O maior peso foi de {maiorpeso}Kg')
print(f'O menor peso foi {menorpeso}')