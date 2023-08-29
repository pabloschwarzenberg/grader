#Cajero Automático
veinte = 20000 * 20
diez = 10000 * 40
cinco = 5000 * 40
cajero = veinte + diez + cinco
print("c",cajero)
saldo = 100000
intentos = 3
print("Saldo de cajero es: ",cajero)
R = input("¿Desea realizar alguna operación en el cajero? s/n: ")
while R != "N":
    usuario = input("Ingrese usuario: ")
    clave = input("Ingrese clave: ")
    if usuario == "10334151":
        if clave == "1803":
            print("Usted tiene $",saldo," en su cuenta.")
            monto = int(input("Ingrese monto a retirar: "))
            if monto <= cajero and monto <= saldo:
                par = monto % 2
                if par == 0 and veinte > 0:
                    cuantos = monto / veinte
                    cuantos_diez = cuantos / diez
                    cuantos_cinco = cuantos_diez / cinco
                    print("billetes 20000=",cuantos)
                    print("billetes 10000=",cuantos_diez)
                    print("billetes 5000=",cuantos_cinco)
                elif par == 0 and veinte == 0:
                    cuantos = monto / diez
                    cuantos_cinco = cuantos / cinco
                    print("billetes 20000=",veinte)
                    print("billetes 10000=",cuantos)
                    print("billetes 5000=",cuantos_cinco)
                elif par == 0 and diez == 0:
                    cuantos = monto / cinco
                    print("billetes 20000=",diez)
                    print("billetes 10000=",diez)
                    print("billetes 5000=",cuantos)
                elif par != 0 and veinte > 0:
                    cuantos = monto / veinte
                    cuantos_diez = cuantos / diez
                    cuantos_cinco = cuantos_diez / cinco
                    print("billetes 20000=",cuantos)
                    print("billetes 10000=",cuantos_diez)
                    print("billetes 5000=",cuantos_cinco)
                elif par != 0 and diez > 0:
                    cuantos_diez = monto / diez
                    cuantos_cinco = cuantos_diez / cinco
                    print("billetes 20000=0")
                    print("billetes 10000=",cuantos_diez)
                    print("billetes 5000=",cuantos_cinco)
                    saldo = saldo - monto
                    print("saldo cuenta=",saldo)
                    print("saldo cajero=",cajero)
            else:
                    print("monto no permitido")
        else:
            print("clave invalida")
            while intentos != 0:
                intentos = intentos - 1
                clave = input("Ingrese clave nuevamente: ")
            if intentos == 0:
                print("tarjeta bloqueada")
                break
    else:
        pass   
    R = input("¿Desea realizar otra operación en el cajero? s/n: ")    