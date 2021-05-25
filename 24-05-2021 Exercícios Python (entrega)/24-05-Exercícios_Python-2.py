#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.
frase = input('Digite a frase desejada: ')
count = 0
vogais = 'aeiouAEIOU'
remover_vogais = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
 
for v in frase:
  if v in 'aeiouAEIOU':
        count += 1
for vogais in remover_vogais:
  frase = frase.replace(vogais, '')

print(f'O total de vogais na frase digitada é: {count}')
print(frase)
