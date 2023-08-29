#Cajero Automático
      
intentos = 0
saldo =100000
saldocaj =1000000


while intentos <=3:
    usuario = input("Introduzca su usuario: ")
    clave = input("Intruduzca su clave: ")

    if clave != "1803":
         print("Vuelva a intentarlo")
         intentos=intentos + 1
    if clave == "1803":
        retirar= int(input("Indique el monto a retirar:"))
        if retirar <= 55000:
            saldofinaldel= (saldo - retirar)
            saldofinalcaj= (saldocaj - retirar)
            print("Saldo Cuenta= {}".format(saldofinaldel))
            print("Saldo cajero= {}".format(saldofinalcaj))
            break
        if retirar >55000:
            print("Monto no permitido")
else:
    print("Tarjeta bloqueada")

    exit()

