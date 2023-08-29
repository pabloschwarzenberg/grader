#Cajero Automático
saldocajero=1000000
saldopersona=100000
c=0
a=input("ingresa usuario")
if a==10334151:
    while True:
        while c<=3:
            c+=1
            b=input("clave")
            if b==1803:
              break
            else:
              print("clave invalida")
        if c==3:
          print("Tarjeta Bloqueada")
          break
        while True:
          w=input("deseas retirar demievo")
          if w!="N":
            break
          else:
              m=int(input("monto"))
              if m<=saldopersona:
                saldopersona-=m
                saldocajero-=m
                print(saldocajero)
                print(saldopersona)
              elif m> saldopersona:
                print("monto invalido")
        break
