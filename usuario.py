from abc import ABC, abstractmethod
from datetime import date

class Usuario(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def mostrar_saldo():
        pass

class Cliente(Usuario):
    def __init__(self, nome, dia_nascimento, mes_nascimento, ano_nascimento, numero_agencia, numero_conta, saldo = 0):
        super().__init__(nome)
        self.numero_agencia = numero_agencia
        self.data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)
        self.numero_conta = numero_conta
        self._saldo = float(saldo)

    def mostrar_saldo(self):
        print(f"O seu saldo é de: R${self._saldo}.")
    
    def depositar(self, valor):
        self._saldo += valor
        print(f"O seu saldo atualizado é de: R$ {self._saldo}")
    
    def sacar(self, valor):
        if valor > self._saldo:
            print(f"Saldo insuficiente para realizar a operação. Consulte o seu saldo e tente novamente.")
        else: 
            self._saldo -= valor
            print(f"Operação realizada com sucesso, o seu saldo atualizado é de: R$ {self._saldo}")

    # O método transferência está em construção. 
    #def transferencia(self, valor, numero_agencia, numero_conta):
    #    if 

class Gerente(Usuario):
    def __init__(self, nome, numero_agencia):
        super().__init__(nome)
        self.numero_agencia = numero_agencia
    
    def mostrar_saldo(numero_conta):
        print(f"O saldo da conta de número: {Cliente.numero_conta} é de: R${Cliente._saldo}")

joao = Cliente("João Victor Nascimento Queiroz Macêdo", 28, 5, 2004, "0001", "000001")
joao.mostrar_saldo()
joao.depositar(1500)
joao.mostrar_saldo()
joao.sacar(1500)
print(joao.data_nascimento)