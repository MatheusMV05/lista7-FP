with open("QP1/qp1.txt", "r") as file:
    linha = file.readlines()
    for i in range(len(linha)):
        ip = linha[i].split(".")
        ip_valido = True
        for x in ip:
            try:
                num = int(x)
                if num < 0 or num > 255:
                    ip_valido = False
                    break
            except ValueError:
                ip_valido = False
                break
        if ip_valido:
            print(linha[i].strip(), "ip valido")
        else:
            print(linha[i].strip(), "ip invalido")