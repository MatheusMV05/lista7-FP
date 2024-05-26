def escrever():
    with open('QP2/QP2.csv', 'w') as file:
        for i in range(6):
            nome = input("Insira nome:")
            file.write(f"{nome}\n")
escrever()

with open('QP2/QP2.csv', 'r') as file:
    lista = file.readlines()
    for i in file:
        lista.append(i)


with open('QP2/Organizado.csv', 'w') as file:
        lista.sort()
        for i in lista:
            file.write(i)





        
