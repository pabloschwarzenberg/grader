#Cajero Automático
saldo=1000000
N="N"
salir=N
b=0
while salir==N :
  usuario=int(input())
  n=0

  if usuario==10334151 :
    clave=int(input())
    contraseña=1803
    
    while clave!=contraseña and n<2 :
        print("clave invalida")
        clave=int(input())
        n=n+1
        
    if clave!=contraseña :
        print("tarjeta bloqueada")

    cuenta=100000
    monto=int(input())

    if monto>cuenta :
        print("monto no permitido")

    else:
        cuenta=cuenta-monto
        saldo=saldo-monto
        while monto>=0 :
          monto=monto-5000
          b=b+1
        print("saldo cuenta=",cuenta)
        print("saldo cajero=",saldo)
        print("billetes 5000=",b-1)
        
        salir=str(input())
    