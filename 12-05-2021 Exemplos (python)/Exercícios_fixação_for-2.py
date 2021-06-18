'''02 - Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), 
conte quantas vezes aparece as vogais a,e,i,o,u'''

frase = (input('Digite uma frase: '))
a = 0
e = 0
i = 0
o = 0
u = 0

for letra in '{frase}':
    if letra == 'a':
        a+= 1
        print(f'A = {a}')

    elif letra == 'e':
        e += 1
        print(f'E = {e}')

    elif letra == 'i':
        i += 1
        print(f'I = {i}')

    elif letra == 'o':
        o += 1
        print(f'O = {o}')

    elif letra == 'u':
        u += 1
        print(f'I = {u}')
    
    