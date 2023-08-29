datos = {"usuario": 1803, "saldo_usuario": 100000,\
     "saldo_cajero": 1000000}

def us_clav(ad):
    cont = 1
    while ad == 0:
        usuario = int(input("usuario"))
        if usuario == 10334151:
            while 0==0:
                clave = int(input("clave"))
                if cont != 3:
                    if clave == datos["usuario"]:
                        ad = 0
                        return True
                    else:
                        cont += 1
                        print("clave invalida")
                        pass
                else:
                    print("tarjeta bloqueada")
                    return False
                    break
            break
        else:
            pass
    

def retiro(salir):
    while salir == False:
        monto = int(input("monto a retirar"))
        if monto <= datos["saldo_cajero"]:
            if monto <= datos["saldo_usuario"]:
                datos["saldo_cajero"] = datos["saldo_cajero"] - monto
                datos["saldo_usuario"] = datos["saldo_usuario"] - monto
                print("saldo cuenta={}\nsaldo cajero={}".format(datos["saldo_usuario"], datos["saldo_cajero"]))
                billetes_(monto)
                salir = input("¿salir?")
                if salir == "N":
                    pass
                else:
                    salir = True      
            else:
                print("monto no permitido")    
        else:
            print("monto no permitido")

    return salir    

billetes = {"billetes 20000 =": 20, "billetes 10000 =": 40, "billetes 5000 =": 40}

def billetes_(monto):
    frase = ""

    a = int(monto/20000)
    b = int((monto - 20000 * a)/10000)
    c = int((monto - 20000 * a - 10000 * b)/ 5000)

    if (a > 0) and (b > 0) and (c > 0):
        frase = list(billetes.keys())[0] + str(a) + list(billetes.keys())[1] + str(b) + list(billetes.keys())[2] + str(c)
    elif (a > 0) and (b > 0) and (c == 0):
        frase = list(billetes.keys())[0] + str(a) + list(billetes.keys())[1] + str(b)
    elif (a > 0) and (b == 0) and (c == 0):
        frase = list(billetes.keys())[0] + str(a)

    elif (a == 0) and (b > 0) and (c > 0):
        frase = list(billetes.keys())[1] + str(b) + list(billetes.keys())[2] + str(c)
    elif (a == 0) and (b > 0) and (c == 0):
        frase = list(billetes.keys())[1] + str(b)

    elif (a > 0) and (b == 0) and (c > 0):
        frase = list(billetes.keys())[2] + str(c)

    billetes["billetes 20000 ="] = billetes["billetes 20000 ="] - a
    billetes["billetes 10000 ="] = billetes["billetes 10000 ="] - b
    billetes["billetes 5000 ="] = billetes["billetes 5000 ="] - c
    
    print(frase)





respuesta = False

while respuesta == False:
    rsp = us_clav(0)
    salir = False

    if rsp == True:
        respuesta = retiro(salir)
    else:
        respuesta = True
        pass
