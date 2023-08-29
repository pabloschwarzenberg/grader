#Cajero Automático
saldo_inicial_cajero=1000000
saldo_usuario=100000
bille=[5000,10000,20000]
salir="N"
while salir=="N":
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
    if monto_a_retirar<saldo_inicial_cajero and monto_a_retirar<saldo_usuario:
      saldo_inicial_cajero=saldo_inicial_cajero-monto_a_retirar
      saldo_usuario=saldo_usuario-monto_a_retirar
      print ("saldo cuenta=",saldo_usuario)
      print("saldo cajero=",saldo_inicial_cajero)
      for i in bille:
        a=0
        p=monto_a_retirar//i
        if p>0:
          for j in range(p):
            monto_a_retirar-=i
            a+=1
        else:
          continue
        print('billetes',i,'=',a)
        if monto_a_retirar==0:
          break
      print('para comletar la acción solicitada se necesita: ',monto_a_retirar)
      break
    else:
      print("el monto indicado no es válido")
  salir=input("¿desea salir? ")