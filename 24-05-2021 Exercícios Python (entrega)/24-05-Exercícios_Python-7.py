#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
numeros_digitados = []
pares = []
impares = []
print('Digite 7 números e eles serão separados entre ímpares e pares.')
for num in range(0,7):
  numeros = int(input('Digite um número: '))
  if numeros % 2 == 0:
    pares.append(numeros) 
  else: 
    impares.append(numeros) 
numeros_digitados.append(pares) 
numeros_digitados.append(impares)
numeros_digitados[0].sort() 
numeros_digitados[1].sort() 
print()
print(f'Os números pares são: {numeros_digitados[0]}')
print(f'Os números ímpares são: {numeros_digitados[1]}')