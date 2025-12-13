from abc import ABC, abstractmethod
from datetime import date
import json

class Usuario(ABC):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    @abstractmethod
    def mostrar_saldo():
        pass

class Cliente(Usuario):
    clientes = {}
    
    def __init__(self, nome, email, dia_nascimento, mes_nascimento, ano_nascimento, numero_agencia, numero_conta, saldo = 0):
        super().__init__(nome, email)
        self.numero_agencia = numero_agencia
        self.data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento)
        numero_conta_corrigido = Cliente.validar_numero_conta(int(numero_conta))
        self.numero_conta = numero_conta_corrigido
        self._saldo = float(saldo)
        Cliente.clientes[self.numero_conta] = self
        Cliente.salvar_clientes()
    
    @classmethod
    def salvar_clientes(cls):
        """Salva todos os clientes em um arquivo JSON"""
        # Carrega dados existentes para mesclar (evita apagar registros não carregados em memória)
        try:
            with open('clientes.json', 'r', encoding='utf-8') as lista_clientes:
                dados = json.load(lista_clientes)
        except (FileNotFoundError, json.JSONDecodeError):
            dados = {}

        # Atualiza/insere clientes atuais em memória sobre os existentes
        for numero_conta, cliente in cls.clientes.items():
            dados[str(numero_conta)] = {
                'nome': cliente.nome,
                'email': cliente.email,
                'numero_agencia': cliente.numero_agencia,
                'data_nascimento': cliente.data_nascimento.isoformat(),
                'saldo': cliente._saldo
            }

        with open('clientes.json', 'w', encoding='utf-8') as lista_clientes:
            json.dump(dados, lista_clientes, indent=4, ensure_ascii=False)
    
    @classmethod
    def validar_numero_conta(cls, numero_conta):
        """Valida e incrementa o número de conta se já existir, evitando duplicatas"""
        numeros_existentes = set()
        
        # Carrega números do arquivo JSON
        try:
            with open('clientes.json', 'r', encoding='utf-8') as lista_clientes:
                dados = json.load(lista_clientes)
                numeros_existentes.update(int(numero_conta) for numero_conta in dados.keys())
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        
        # Adiciona números em memória
        numeros_existentes.update(cls.clientes.keys())
        
        # Se o número já existe, incrementa até encontrar um disponível
        while numero_conta in numeros_existentes:
            numero_conta += 1
        
        return numero_conta

    def mostrar_saldo(numero_conta):
        """Mostra o saldo"""
        print(f"O seu saldo é de: NULL")
    
    def depositar(self, valor):
        self._saldo += float(valor)
        print(f"O seu saldo atualizado é de: R$ {self._saldo}")
    
    def sacar(self, valor):
        if float(valor) > self._saldo:
            print(f"Saldo insuficiente para realizar a operação. Consulte o seu saldo e tente novamente.")
        else: 
            self._saldo -= float(valor)
            print(f"Operação realizada com sucesso, o seu saldo atualizado é de: R$ {self._saldo}")

    # O método transferência está em construção. 

#A seguinte classe está em construção.
#class Gerente(Usuario):
#    def __init__(self, nome, numero_agencia):
#        super().__init__(nome)
#        self.numero_agencia = numero_agencia
#    
#    def mostrar_saldo(numero_conta):
#        print(f"O saldo da conta de número: {Cliente.numero_conta} é de: R${Cliente._saldo}")