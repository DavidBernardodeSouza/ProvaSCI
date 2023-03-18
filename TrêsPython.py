while True:
    # Solicitação do nome do aluno e das quatro notas
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))

    # Cálculo da média
    media = (nota1 + nota2 + nota3 + nota4) / 4

    # Impressão do resultado
    print("Aluno:", nome)
    print("Média:", media)

    if media >= 6:
        print("Aprovado")
    else:
        print("Reprovado")

    # Verificação se deseja continuar ou encerrar o programa
    opcao = input("Deseja continuar? (s/n): ")
    if opcao.lower() == "n":
        break