#Cajero Automático
cont=1
while (cont<=3):
    usuario = int(input(""))
    clave = int(input(""))
         if (usuario==10334151 and clave=1803) == True:
             break
         else:
             print("clave invalida")
             cont=cont+1
         if cont==4:
            print("tarjeta bloqueada")
            break

retirar = int(input("¿Cuál es el monto que desea retirar?"))

if retirar >100000:
    print("monto no permitido")

saldo_cuenta=100000-retirar
saldo_cajero=1000000-retirar

if retirar<=100000:
    print("saldo cuenta=", saldo_cuenta)
    print("saldo cajero=", saldo_cajero)