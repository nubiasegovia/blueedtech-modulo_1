'''For (laço/para) = laço for tem uma variável de controle, a condição tem
 um começo e um fim. Repete algo'''

for c in range(1, 6,): #para contador dentro do intervalo de 1 a 5 faça - o último número que colocar não aparece- , range ignora o último caractere
    print('Olá')
print('Fim')

#contagem regressiva
for c in range(10, -1, -1): 
    print(c)
print('Fim')

#pedir para usuário digitar número
n = int(input('Digite um número: '))

for c in range(0,n+1):
    print(c)
print('Fim.')

#quero saber do usuário o início e o final
i = int(input('Início: '))
f = int(input('Final: '))
p = int(input('Passos:'))

for c in range (i, f+1, p):
    print(c)

print(f'A soma dos números é: {soma}')


#Repetir um input 
soma = 0

for c in range(0, 4): #0, 1, 2, 3
    n = int(input('Digite um número para soma: '))
    soma += n

print(f'A soma dos números é: {soma}')

#Opções para for além de range
for c in 'Thiago': # T = 0, h = 1, i = 2, a = 3, g = 4, o = 5

#if dentro do for

for contador in 'Thiago':
    if contador == 'a':
        print('A letra A existe!')
        