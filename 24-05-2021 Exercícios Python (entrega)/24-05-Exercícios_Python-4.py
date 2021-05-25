#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no formato
#  DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 'data inválida' caso a data seja inválida.

def mes_extenso():
    mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    dd = int(input('Informe o dia no formato DD : '))
    mm = int(input('Informe o mês no formato MM : '))
    ano = int(input('Informe o ano no formato AAAA: '))
    print(f'A data informada foi: {dd}/{mm}/{ano}')
    print(f'{dd} de {mes[mm -1]} de {ano}')


mes_extenso()