#Cajero Automático
saldoca = 1000000
saldou = 100000
usuario = "10334151"
clave = "1803"
intentos = 3
seguir = True
while(seguir):
    u = input("ingrese usuario: ")
    if(u != usuario):
        print("usuario no identificado")
    else:
        seguir = False
        for i in range(0,intentos):
            c = input("ingrese clave: ")
            if(c != clave):
                print("clave invalida")
                intentos = intentos-1
                if(intentos == 0):
                    print("tarjeta bloqueada")
                    seguir = False
                    break
            elif(c == clave):
                print("su monto son 100.000")
                seguir2 = True
                while(seguir2):
                    monto = int(input("ingrese monto que desea girar: "))
                    if(monto>100000):
                        print("monto no permitido")
                    else:
                        saldoca = saldoca-monto
                        saldou = saldou-monto
                        print("saldo cuenta =",saldou)
                        print("saldo cajero =",saldoca)

                        cont = input("desea continuar: ")
                        if(cont!="N"):
                            seguir = False
                            seguir2 = False
            break