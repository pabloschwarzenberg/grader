#Cajero Automático
cuenta = int(100000)
cajero = int(1000000)
contador = 0
def cajeroa(usuario,clave,monto):
    if usuario == 10334151 and clave == 1803 and monto > cuenta:
        return True
    if usuario == 10334151 and clave == 1803 and monto > cajero:
        return True
    if usuario == 10334151 and clave != 1803:
        contador += 1
        return True
    if contador == 3:
        return False
    

while True:
    try:
        usuario = int(input("Ingresar su usuario :"))
        clave = int(input("Ingresar clave :"))
        if usuario == 10334151 and clave != 1803:
            contador += 1
            print("clave invalida")
        else:
            monto = int(input("Ingresar el monto a retirar :"))
        
        if monto > cajero or monto > cuenta:
            print("monto no permitido")
            break
        else:
            print("saldo cuenta=",cuenta - monto)
            print("saldo cajero=",cajero - monto)
            
        salir = input("Si desea salir presione algo diferente a N :")
        if salir != "N":
            break
    except:
        print("tarjeta bloqueada")
        break      