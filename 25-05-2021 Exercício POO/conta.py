""" 
 e os métodos Sacar e Depositar. Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ Adicione uma regra no
 método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, caso contrário mostre a mensagem na tela: "Você não tem 
 saldo suficiente para essa operação." """

class Conta: 
    def __init__(self, Titular, Saldo=0):
        self.titular = Titular
        self.saldo = Saldo

    def Saque(self, sacar):
        sacar = int(input('Digite o valor para saque: '))
        if sacar != 0:
            if sacar > self.saldo: 
                print(f'Você não tem saldo suficiente para essa operação. Disponível para saque: R$ {self.saldo:.2f}')
            else: 
                self.saldo -= sacar
                print(f'Saque efetuado com sucesso. Saldo atual: R$ {self.saldo:.2f}')
        else:
            print('Você não pode sacar 0 reais.')
            

    def Deposito(self, depositar):
        depositar = int(input('Digite o valor para depósito: '))
        self.saldo += depositar
        print(f'Depósito efetuado com sucesso! Saldo total: {self.saldo}')



  