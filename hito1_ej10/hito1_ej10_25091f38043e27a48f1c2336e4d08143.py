#Cajero Automático
saldo=1000000
i=0
while i<3:
    usuario=int(input("usuario"))
    clave=int(input("clave"))
    if usuario==10334151 and clave==1803:
        monto=int(input("monto a retirar"))
        if monto>100000:
          print("monto no permitido")
          break
        elif monto<=100000:
          sc=100000-monto
          sj=saldo-monto
          print("saldo cuenta= ",str(sc))
          print("saldo cajero= ",str(sj))
          break
    elif usuario!=10334151 and clave!=1803:
                  print("clave invalida")
                  i+=1
print("tarjeta bloqueada")                        