arquivo = "QP3/QP3.txt"

def nomes(arquivo):
    with open(arquivo, 'w') as file:
        for i in range(6):
            nome = input("Insira o nome e sobrenome:")
            file.write(nome+"\n")

def alterar(arquivo):
    nomes(arquivo)
    with open(arquivo, 'r') as file:
        lines = file.readlines()

    for i, linha in enumerate(lines):
        print(linha, end="")
        alt = input("Deseja modificar(s/n)?").lower()
        if alt == 's':
            lines[i] = input("Insira o novo nome:") + "\n"

    with open(arquivo, 'w') as file:
        file.writelines(lines)

alterar(arquivo)