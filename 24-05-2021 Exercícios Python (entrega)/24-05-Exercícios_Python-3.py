#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.
from random import randint
import os

senha = 'goblue'
tentativas = 0
login = input('digite a sua senha: ')
n_aleatorio = randint(0,10)
n_usuario = 0
c = 0
while login != senha :
    print('Acesso acesso negado, tente novamente: ')
    tentativas +=1
    login = input('digite a sua senha: ')
    if login == senha:
      break
print('Acesso permitido, seja bem vindo(a)!')
print('''
Agora, temos um jogo de adivinhação para passar o tempo! Preparado(a) para o meu desafio? 
Eu pensei em um número de 0 a 10, consegue descobrir qual foi?
 ''')
while n_aleatorio != n_usuario:
    n_usuario = int(input('Em qual número eu pensei? '))
    c += 1
    
print(f'Parabéns, conseguiu acertar! Você precisou de {c} chances para descobrir o valor')
