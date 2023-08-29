#Cajero Automático
si=1000000
su=100000
usuario=input("ingrese usuario: ")
clave=input("ingrese clave: ")
letra=str()
letra="n"
i=1

while letra=="N" or letra=="n" and su >=1:
                            
        if usuario == "10334151":
            if i==1 or i==2 or i==3:
                if clave == "1803":
                    montor=int(input("monto a retirar: "))
                    if montor < 100000:
                        su = su - montor
                        si = si - montor
                        print("{}{}{}{}".format("saldo cuenta=", su, "saldo cajero=", si))
                    else:
                        print("monto no permitido")
                        break
                else:
                    print("clave inválida")
                    clave=input("ingrese clave: ")
                    i += 1
            else:
                print("Tarjeta bloqueada")
                break
        else:
            print("Usuario inválido")
            break
        letra=input("Para salir del Cajero no digite letra N: ")
        if letra!="N" or letra!="n":
                break
        