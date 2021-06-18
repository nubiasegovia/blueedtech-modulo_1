#04 - Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.

frase = (input('Digite uma frase: ')).lower()
vogais = 'aeiou'

for i in vogais:
    frase = frase.replace(i, '')

print(frase)
