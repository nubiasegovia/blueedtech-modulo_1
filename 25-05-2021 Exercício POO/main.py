from conta import Conta

nome = str(input('Digite o nome do titular: '))
saldo = float(input('Digite o saldo da conta: '))


cliente1 = Conta('Núbia', 39000) 
cliente2 = Conta(nome, saldo)

while True:
    cliente2.Saque('sacar')
    resp = str(input('Quer continuar sacando? [S/N] ').strip().upper()[0])
    if resp in 'N':
        break
