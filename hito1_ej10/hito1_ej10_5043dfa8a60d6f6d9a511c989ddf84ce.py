def cajero():
  usuario=int(input())
  clave=int(input())
  saldo_cajero=1000000
  saldo_usuario=100000
  b=0
  while clave!=1803:
    b+=1
    if b==3:
      print("tarjeta bloqueada")
      cajero()
    else:
      print("clave invalida")
    clave=int(input())

  while clave==1803:
    retira=int(input())
    while retira>saldo_usuario or retira>saldo_cajero:
      print("monto no permitido")
      retira=int(input())
    if retira<=saldo_usuario:
      saldo_usuario-=retira
      saldo_cajero-=retira
      salir=str(input())
      if saldo_usuario==0 or salir!="N":
        cajero()
    print("saldo cuenta=",saldo_usuario)
    print("saldo cajero=",saldo_cajero)        
cajero()
