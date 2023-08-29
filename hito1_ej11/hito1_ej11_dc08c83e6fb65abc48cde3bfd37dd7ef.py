respuesta="N"
import random
n=0
saldo=10**5
saldo_cajero=10**6
while respuesta=="N":
    while n<3:
        usuario = int(input("usuario: "))
        clave = int(input("contraseña: "))
        if usuario==10334151 and clave==1803:
            n=n+10
        else:
            print("clave invalida")
            n=n+1
    if n==3:
        print("tarjeta bloqueada")
        respuesta=str("N1")
    if n!=3:
        monto_retirar = int(input("monto deseado: "))
        
        if monto_retirar>saldo or monto_retirar>saldo_cajero :
            print("monto invalido")
            respuesta=input("quiere realizar otra operacion? ")
          
        else:
            saldo=saldo-monto_retirar
            saldo_cajero=saldo_cajero-monto_retirar
            print("saldo cuenta={0}".format(saldo))
            print("saldo cajero={0}".format(saldo_cajero))
            respuesta=input
            i=1
            n=2
            while i < n:
              n20 = random.randint(1, 20)
              n10 = random.randint(1, 40)
              n5 = random.randint(1, 40)
              suma = ((n20*20000)+(n10*10000)+(n5*5000))
              if monto_retirar == suma:
                print("billetes 20000={}".format(n20))
                print("billetes 10000={}".format(n10))
                print("billetes 5000={}".format(n5))
                break
              

      