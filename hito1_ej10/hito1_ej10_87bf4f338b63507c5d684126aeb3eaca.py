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
    r = eval(input("ingrese la cantidad a retirar: "))
    while (0 > r) or (r > sca) or (r > scu):
        print("monto no permitido ingreselo nuevamente")
        r = eval(input("ingrese la cantidad a retirar:"))
    while (sca >= r > 0) and (scu > r > 0):
        print("monto permitido")
        print("se a retirado $",r)
        scu = scu - r
        sca = sca - r
        print("saldo de la cuenta:",scu)
        print("saldo del cajero:",sca)
        s = input("desea salir? S/N:")
        if (s == "N"):
            r = eval(input("ingrese la cantidad a retirar:"))
            while (0 > r) or (r > sca) or (r > scu):
                print("monto no permitido ingreselo nuevamente")
                r = eval(input("ingrese la cantidad a retirar:"))
            while (sca > r > 0) and (scu > r > 0):
                print("monto permitido")
                print("se a retirado $",r)
                scu = scu - r
                sca = sca - r
                print("saldo de la cuenta:",scu)
                print("saldo del cajero:",sca)
                s = input("desea salir? S/N:")
        elif (s != "N"):
            print("cerrando el programa")
        break
