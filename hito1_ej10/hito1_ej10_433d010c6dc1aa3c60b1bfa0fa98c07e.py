#Cajero Automático
saldocajero=1000000
saldousuario=100000
intentos=3
salida="N"

while((intentos>0)and(salida=="N")):
    usuario=input("Indique su codigo de usuario:\n")
    clave=input("Por favor, introduzca su clave:\n")

    if(clave!="1803"):
        intentos=intentos-1
        print("Clave erronea")
    elif(usuario!="10334151"):
        print("Usuario no encontrado")
    else:
        print("Saldo cajero:",saldocajero)
        print("Saldo cuenta:",saldousuario)
        retiro=int(input("Monto a retirar: "))
        saldocajero=saldocajero-retiro
        saldousuario=saldousuario-retiro

        frase1="saldo cuenta"+"="+str(saldousuario)
        frase2="saldo cajero"+"="+str(saldocajero)
        print(frase1)
        print(frase2)
    salida=input("¿Deseas realizar otra operación?\nMarca con cualquier letra menos la N para continuar:")

      