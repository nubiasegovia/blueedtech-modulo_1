'''Um professor, muito legal, fez 3 provas durante um semestre, mas só vai levar em conta as 
duas notas mais altas para calcular a média.
Faça uma aplicação que peça o valor das 3 notas, mostre como seria a média com essas 3 
provas, a média com as 2 notas mais altas, bem como sua nota mais alta e sua nota mais baixa.'''

def notas(a, b, c):
    med = (a + b + c) / 3 
    print(f'A média das três notas seria: {med}')
    lista = [a, b, c]
    min(lista)
    med_altas = ((a + b + c) - (min(lista))) / 2
    max(lista)
    print(f'A nota mais alta foi: {max(lista)}')
    print(f'A média com as duas notas mais alta é: {med_altas}')
    print(f'A nota mais alta foi: {max(lista)}')


