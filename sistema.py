import os
import subprocess
import usuario

def limpar():
    cmd = "cls" if os.name == "nt" else "clear"
    subprocess.call(cmd, shell = True)

def enter():
    input("Pressione Enter para continuar.")

def titulo_pagina():
    print("* * * * * * * * * * * * * * * * * * * * Banco Píton * * * * * * * * * * * * * * * * * * * *")

opcao = None
while opcao != 0:
    limpar()
    print("* * * * * * * * * * Bem vindo ao Banco Píton * * * * * * * * * * ")
    opcao = int(input("Digite a opção desejada:\n1 - Abrir conta\n2 - Verificar saldo\n3 - Sacar\n4 - Depositar\n0 - Sair\n"))
    if opcao == 1:
        limpar()
        titulo_pagina()
        nome = input("Insira o seu nome: ")
        dia_nascimento = int(input("Insira o dia do seu nascimento: "))
        mes_nascimento = int(input("Insira o mês do seu nascimento: "))
        ano_nascimento = int(input("Insira o ano do seu nascimento: "))
        cliente = usuario.Cliente(nome, dia_nascimento, mes_nascimento, ano_nascimento, "0001", "000001")
        print(f"A sua conta no Banco Píton foi aberta com sucesso! Seja bem vindo(a) {cliente.nome} é um prazer tê-lo(a) conosco.")
        enter()
    
    elif opcao == 2:
        limpar()
        titulo_pagina()
        usuario.Cliente.mostrar_saldo(cliente)
        enter()

    
    elif opcao == 3:
        limpar()
        titulo_pagina()
        valor = input("Por favor, digite o valor desejado: ")
        usuario.Cliente.sacar(cliente, valor)
        enter()


    elif opcao == 4:
        limpar()
        titulo_pagina()
        valor = input("Por favor, digite o valor desejado: ")
        usuario.Cliente.depositar(cliente, valor)
        enter()

    
    elif opcao == 0:
        limpar()
        print("* * * * * * * * * * * * * * * * * * * * Banco Píton * * * * * * * * * * * * * * * * * * * *" \
        "\nObrigado por utilizar os serviços do Banco Píton. Até logo." \
        "\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
        break

    else:
        titulo_pagina()
        print("Opção inválida, por favor digite a opção desejada novamente.")
        enter()