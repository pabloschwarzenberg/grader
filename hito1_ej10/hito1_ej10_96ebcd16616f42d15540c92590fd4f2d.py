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

respuesta = False

while respuesta == False:
    rsp = us_clav(0)
    salir = False

    if rsp == True:
        respuesta = retiro(salir)
    else:
        respuesta = True
        pass


