arquivo = 'QP4/QP4.txt'
cont_nom = {}
with open(arquivo, 'w') as file:
    while True:
        nome = input("Digite o nome do aluno ou (sair) para sair:").lower()  
        if nome == 'sair':
            break 
        file.write(nome + '\n')
    
with open(arquivo, 'r') as file:
     nomes = file.readlines()

nomes = [nome.strip() for nome in nomes]

for nome in nomes:
    if nome in cont_nom:
        cont_nom[nome] += 1
    else:
        cont_nom[nome] = 1

for nome, contagem in cont_nom.items():
    print(f"Nome: {nome}, Quantidade: {contagem}")
