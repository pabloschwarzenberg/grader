#Cajero Automático
def cajero():
    i=0
    while i<3:
        x=int(input("ingrese su nombre de usuario: "))
        i=i +1
        if x==10334151:
                print("usuario correcto")
                y=input("ingrese su clave: ")
                if y=="1803":
                    print("Bienvenido")
                    a = int(input("ingrese el monto que desea retirar: "))
                    if a>100000:
                        print("monto no permitido")
                    else:
                        if a<=100000:
                            print("saldo cuenta=",100000-int(a))
                            print("saldo cajero=",1000000-int(a))
                            billetes = (20000, 10000, 5000)
                            for i in billetes:
                                tipo, plural = "billete", ""
                                b = a / i
                                if b >= 1:
                                    if int(b) > 1: plural = "s"
                                    print(tipo + plural + " " + str(i) + "=" + str(int(b)))
                                    a %= i


                            break
                else:
                    print("clave invalida")
                    if    i==3:
                            print("tarjeta bloqueada")
                            break
        else:
                print("usuario incorrecto")
                if    i==3:
                    print("intentos agotados")

cajero()