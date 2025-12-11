import usuario

opcao = None
while opcao != 0:
    print("* * * * * * * * * * Bem vindo ao Banco Píton * * * * * * * * * * ")
    opcao = int(input("Digite a opção desejada:\n1 - Abrir conta\n2 - Verificar saldo\n3 - Sacar\n4 - Depositar\n0 - Sair\n"))
    if opcao == 1:
        print("* * * * * * * * * * Bem vindo ao Banco Píton * * * * * * * * * * ")
        nome = input("Insira o seu nome: ")
        dia_nascimento = input("Insira o dia do seu nascimento: ")
        mes_nascimento = input("Insira o mês do seu nascimento: ")
        ano_nascimento = input("Insira o ano do seu nascimento: ")
        cliente = usuario.Cliente(nome, dia_nascimento, mes_nascimento, ano_nascimento, "0001", "000001")
        print(f"A sua conta no Banco Píton foi aberta com sucesso! Seja bem vindo(a) {cliente.nome} é um prazer tê-lo(a) conosco.")