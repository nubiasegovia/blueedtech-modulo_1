#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
   # A soma deles;
   # A multiplicação entre eles;
   # A divisão inteira deles;
   # Mostre na tela qual é o maior;
   # Verifique se o resultado da soma é par ou impar e mostre na tela;
   # Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.

from math import prod #Importação de biblioteca para fazer a multiplicação dos elementos da lista


numeros = []
for c in range(1, 2+1): #Repetir duas vezes o input. 2+1 porque quero que o último número seja adicionado.
    numeros.append ( int(input('Digite o número desejado: ')))
divint = numeros[0] // numeros[1] #Divisão inteira dos dois números dentro da lista
soma = sum(numeros) #Sum faz a soma de todos os elementos dentro da lista
print()
print(f'Os números digitados foram: {numeros}')
if soma == 0: 
    print(f'A soma deles é {soma}, um número par')
else:
    print(f'A soma deles é {soma}, um número ímpar ')
print(f'O resultado da multiplicação entre eles é: {prod(numeros)}') #Prod faz a multiplicação de todos os elementos na lista
print(f'O resultado da divisão inteira deles é: {divint} ')
if numeros[0] > numeros[1]:
    print(f'O maior número é {numeros[0]}')
else:
    print(f'O maior número é {numeros[1]}')
if prod(numeros) > 40:
    maior40 = prod(numeros) / divint
    print(f'A multiplicação entre os números foi maior que 40 e ao fazer a divisão inteira deles, o resultado foi {maior40}')
else: 
    print(f'A multiplicação de {numeros[0]} e {numeros[1]} não foi maior que 40')

