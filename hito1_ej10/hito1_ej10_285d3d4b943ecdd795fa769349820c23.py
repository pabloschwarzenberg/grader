u = int(input("ingrese el usuario:"))
c = int(input("ingrese la clave:"))
m = 3
scu = 1000000
sca = 100000

while (c != 1803) and (u == 10334151) and (m > 1):
    m = m-1
    print("clave invalida intentelo denuevo")
    u = int(input("ingrese el usuario:"))
    c = int(input("ingrese la clave:"))
    if (m == 1):
        print("targeta bloqueada")
        
while (c == 1803) and (u != 10334151) and (m > 1):
    m = m-1
    print("usuario invalido intentelo denuevo")
    u = int(input("ingrese el usuario:"))
    c = int(input("ingrese la clave:"))
    if (m == 1):
        print("targeta bloqueada")
while (c == 1803) and (u == 10334151):
    print("clave valida")
    r = int(input("ingrese la cantidad a retirar:"))
    if (0 > r) or (r > sca) or (r > scu):
        print("monto no permitido ingreselo nuevamente")
        r = int(input("ingrese la cantidad a retirar:"))
    elif (sca >= r > 0) and (scu > r > 0):
        print("monto permitido")
        print("se a retirado $",r)
        scu = scu - r
        sca = sca - r
        print("saldo cuenta=",sca,",","saldo cajero=",scu)
        s = input("desea salir? S/N:")
        if (s == "N"):
            r = int(input("ingrese la cantidad a retirar:"))
            if (0 > r) or (r > sca) or (r > scu):
                print("monto no permitido ingreselo nuevamente")
                r = inrt(input("ingrese la cantidad a retirar:"))
            elif (sca > r > 0) and (scu > r > 0):
                print("monto permitido")
                print("se a retirado $",r)
                scu = scu - r
                sca = sca - r
                print("saldo cuenta=",sca,",","saldo cajero=",scu)
                s = input("desea salir? S/N:")
        elif (s != "N"):
            print("cerrando el programa")
        break
