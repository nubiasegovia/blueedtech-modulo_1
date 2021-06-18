# Listas compostas são listas dentro de listas, com os conceitos ensinados anteriormente, nós conseguimos criar a seguinte lista:

pessoa = list()
pessoa.append('Anna')
pessoa.append(40)

print(pessoa)

# Esse código acima gera um conjunto de dados na mesma lista, porém se eu adicionar mais dados de nome e idade na mesma lista, isso pode nos confundir na hora de apresentar esses dados ou buscar esses dados. Vai ser dificil saber que idade pertence a qual nome, por isso temos as listas compostas. Vamos criar uma lista que receba varias listas com nome e idade:

#Para criar uma lista composta eu coloco a lista pessoa dentro da lista povo:
povo = list()
povo.append(pessoa[:]) # Se eu atribuir sem ess [:] ele cria uma ligação e não uma cópia

# Agora para adicionar novas listas pessoa dentro da lista povo, eu adiciono mais itens nas posições da lista pessoa:

pessoa[0] = 'Maria'
pessoa[1] = 18

# E agora eu adicono a lista pessoa de novo na lista povo:

povo.append(pessoa[:])
print(povo)

# Outra forma de criar listas compostas é:

povoado = [['Anna', 40], ['Maria', 18], ['José', 34], ['Roberta', 56]]
print(povoado)

print(povoado[0][0]) # Mostre a lista na posição 0, e o dado na posição 0 dessa lista.
print(povoado[0][1]) # Mostre a lista na posição 0, e o dado na posição 1 dessa lista.
print(povoado[1][1]) # Mostre a lista na posição 1, e o dado na posição 1 dessa lista.
print(povoado[3][0]) # Mostre a lista na posição 3, e o dado na posição 0 dessa lista.
print(povoado[2][1]) # Mostre a lista na posição 2, e o dado na posição 1 dessa lista.

# Vamos utilizar o for para varrer essa lista:

for p in povoado:
   print(p[0]) # Mostra apenas os nomes dessas listas.
   print(f'{p[0]} tem {p[1]} anos de idade.')


# Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' e  também quantos são maiores e quantos são menores de idade.

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,5):
   dado.append(str(input('Nome: ')))
   dado.append(int(input('Idade: ')))
   galera.append(dado[:])
   dado.clear() # Limpa a lista dados, para receber outros dados na próxima rodada

for p in galera:
   if p[1] >= 18:
      print(f'{p[0]} é maior de idade')
      totmai += 1
   else:
      print(f'{p[0]} é menor de idade')
      totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
