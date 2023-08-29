#Cajero Automático
saldoinicial_cajero=1000000
saldo_usuario=100000
salir="S"
while salir=="S":
  intentos= 3
  usuario=input("ingrese usuario: ")
  while intentos>0:
      
    clave=input("ingrese clave: ")
    if usuario=="10334151" and clave=="1803":
        print("Bienvenido")
        break
    elif clave!="1803" or usuario!="10334151":
        intentos=intentos-1
        print("usuario o clave inválida")
  if intentos==0:
    print("tarjeta bloqueda")
  else:
    monto_a_retirar=int(input("ingrese monto a retirar: "))
    if monto_a_retirar<saldoinicial_cajero and monto_a_retirar<saldo_usuario:
      saldoinicial_cajero=saldoinicial_cajero-monto_a_retirar
      saldo_usuario=saldo_usuario-monto_a_retirar
      print ("saldo cuenta=",saldo_usuario)
      print("saldo cajero=",saldoinicial_cajero)
    else:
      print("el monto indicado no es válido")
  salir=input("¿quiere terminar la operacion? ")