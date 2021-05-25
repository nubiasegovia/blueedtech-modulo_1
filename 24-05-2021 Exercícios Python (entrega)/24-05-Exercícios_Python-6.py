#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

perguntas = []

print('Vamos dar início às perguntas... Para cada uma responda com "Sim" ou "Não". ')
perguntas.append ( (input('Telefonou para a vítima? ')).upper().strip()[0] ) 
perguntas.append ( (input('Esteve no local do crime? ')).upper().strip()[0] )
perguntas.append ( (input('Mora perto da vítima? ')).upper().strip()[0] )
perguntas.append ( (input('Devia para a vítima? ')).upper().strip()[0] )
perguntas.append ( (input('Já trabalhou com a vítima? ')).upper().strip()[0] )

if perguntas.count('S') == 2:
    print('Suspeita')
elif perguntas.count('S') == 3 or perguntas.count('S') == 4:
    print('Cúmplice')
elif perguntas.count('S') == 5:
    print('Assassino')
else: 
    print('Inocente')

