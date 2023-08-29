saldocajero=1000000
saldocuenta=100000
i=0
while i<3:
  usuario=int(input("ingrese su nombre de usuario",))
  if usuario==10334151:
    clave=int(input("ingrese su clave de usuario",))
    if clave==1803:
      mar=int(input("monto a retirar"))
      if mar<=saldocuenta and mar>=0:
        saldocuenta=saldocuenta-mar
        saldocajero=saldocajero-mar
        print ("saldocuenta=" , saldocuenta ,"," , "saldo cajero=" , saldocajero)
        esc=str(input("para salir la debe ingresar algo distinto a la letra N"))
        if esc != "N":
          break
      else:
        print("monto no permitido")
    elif clave != 1803:
      i=i+1
      if i==3:
        print("tarjeta bloqueda")
        break