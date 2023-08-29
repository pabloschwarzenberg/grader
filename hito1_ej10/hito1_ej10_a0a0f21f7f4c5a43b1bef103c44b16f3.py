#Cajero Automático
saldoCajero =1000000
usuarioCajero = 10334151
claveusuario = 1803
dineroUsuario = 100000
intento = 1
N = True
while N:
      usuario = int(input("usuario :"))
      while usuarioCajero != usuario:
            usuario = int(input("usuario :"))
      while intento<=3:
            clave = int(input("clave :"))
            if clave != claveusuario:
                  print("clave invalidad")
                  intento += 1
            elif clave == claveusuario:
                  break
      if intento > 3:
            print("tarjeta bloqueada")
            N = False
            break
      print("monto a retirar ")
      monto = int(input("="))
      while monto>dineroUsuario or monto > saldoCajero:
            print("monto no permitido")
            monto = int(input("ingrese monto valido :"))
      else:
            saldoCajero -= monto
            dineroUsuario -= monto
            print("saldo en cuenta =",dineroUsuario)
            print("saldo cajero =",saldoCajero)

      continuar = input("presione N para realizar otra operacion")
      continuar = continuar.upper()
      if continuar != "N":
            N = False
