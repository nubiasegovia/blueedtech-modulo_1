'''Exercício Treino 2 - Escreva uma função que recebe dois números (a e b) como parâmetro e 
retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.'''

def nums(n1, n2):
    if n1 > n2:
        print(n2)
    elif n1 < n2 :
        print(n1)
    else:
        print('Valores idênticos!')



n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))

num(n1, n2)