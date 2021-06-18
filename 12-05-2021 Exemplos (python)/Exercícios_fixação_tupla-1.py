'''01 - Crie um programa que vai gerar cinco números aleatórios de 1 a 50 e colocar em uma  tupla. Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla. Sem utilizar repetições. Dica: utilizar a biblioteca random do Python.'''

import random
n1 = random.randint(1,50)
n2 = random.randint(1,50)
n3 = random.randint(1,50)
n4 = random.randint(1,50)
n5 = random.randint(1,50)

numeros = (n1, n2, n3, n4, n5)

print(f'Os números gerados foram {numeros}')
print(f'O menor número é: {min(numeros)}')
print(f'O maior número é: {max(numeros)}')