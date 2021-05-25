#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
from datetime import datetime

ano_atual = datetime.now().year
trabalhador = dict()
trabalhador['nome'] = str(input('Digite o seu nome: '))
ano_nascimento = int(input('Ano de nascimento[AAAA]: '))
trabalhador['idade'] = datetime.now().year - ano_nascimento
trabalhador['ctps'] = int(input('Informe o nº da CTPS: '))
if trabalhador['ctps'] != 0:
    trabalhador['ano_contratacao'] = int(input('Qual o ano de contratação? '))
    trabalhador['salario'] = float(input('Informe o salário: R$'))
    trabalhador['idade_aposentadoria'] = trabalhador['idade'] + ((trabalhador['ano_contratacao'] + 35) - datetime.now().year)
print()
for k, v in trabalhador.items():
    print(f' {k} : {v}')
    
