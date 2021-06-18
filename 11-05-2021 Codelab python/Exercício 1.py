
'''Exercício Treino 1 - Escreva uma função que recebe dois parâmetros (números) e imprime o 
menor dos dois. Se eles forem iguais, imprima que são valores idênticos.'''

def num(n1, n2):
    if n1 > n2:
        print(n2)
    elif n1 < n2 :
        print(n1)
    else:
        print('Valores idênticos!')



n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

num(n1, n2)
