with open("QP1/qp1.txt", "r") as file:
    ips = []
    lines = file.readlines()
    for i in lines:
        ips.append(i.strip())
    for i in range(len(ips)):
        ip = ips[i].split(".")
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
            print(ips[i], "ip valido")
        else:
            print(ips[i], "ip invalido")