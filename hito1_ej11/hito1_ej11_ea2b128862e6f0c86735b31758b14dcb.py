#Cajero Automático
#Cajero Automático
saldo_cajero = 1000000
saldo_usuario = 100000
usuario_correcto="10334151"
clave_correcta="1803"
monto_minimo="1"
monto_maximo="99999"

billetes_20mil= 20
billetes_10mil= 40
billetes_5mil = 40


usuario =str(int(input("Ingrese su usuario: ")))
clave   =str(int(input("Ingrese la contraseña: ")))
while True:
    if (usuario==usuario_correcto) and (clave==clave_correcta):
      monto= str(int(input("Ingrese el monto a retirar: ")))

      if (monto>=monto_minimo) and (monto<=monto_maximo):
        monto=int(monto)
        total_cuenta  = saldo_usuario - monto
        total_usuario = saldo_cajero  - monto
        print("saldo cuenta=",total_cuenta)
        print("saldo cajero=",total_usuario)

        expulsar_20mil=int(monto//20000)
        monto=monto%20000
        expulsar_10mil=int(monto//10000)
        monto=monto%10000
        expulsar_5mil=int(monto//5000)
        monto=monto%5000

        print("billetes 20000=",expulsar_20mil)
        print("billetes 10000=",expulsar_10mil)
        print("billetes 5000=",expulsar_5mil)
        break
      
      elif (monto<monto_minimo) and (monto>monto_maximo):
        print("monto no permitido")
        False

      elif (monto!="N"):
        break

    if (usuario!=usuario_correcto) or (clave!=clave_correcta):
        print("clave invalida")
        clave=str(int(input("Ingrese la contraseña: ")))

        if (usuario!=usuario_correcto) or (clave!=clave_correcta):
          print("clave invalida")
          clavelave=str(int(input("Ingrese la contraseña denuevo: ")))

          if (usuario!=usuario_correcto) or (clave!=clave_correcta):
            print("tarjeta bloqueada")
            break