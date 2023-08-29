
saldo_inicial=1000000
saldo_persona=100000
intentos=0
algo="n"
while algo == "n":
  usuario=int(input())
  clave=int(input())
  while intentos < 3:
      if usuario == 10334151 and clave == 1803:
        monto=int(input("monto a retirar:  "))
        if monto > saldo_inicial or monto > saldo_persona:
          print("monto no permitido")
          algo=input("quiere realizar otra operacion? ")
          
        else:
          saldo_inicial=saldo_inicial-monto
          saldo_persona=saldo_persona-monto
          print("saldo cuenta","=",saldo_persona)
          print("saldo cajero","=",saldo_inicial)
          algo=input()
      else:
        print("clave invalida")
        intentos=intentos+1
        algo="n1"
  if intentos == 3:
    print("tarjeta bloqueada")

  
  