#aprobación de creditos
sui=100000
sci=1000000
opcion=0
while(opcion==0):
    u="usuario 10334151"
    print(u)
    c=int(input("ingrese la clave: "))
    contador = 0
    while (c != 1803 and contador < 3):
        print("clave invalida")
        c = int(input("ingrese la clave nuevamente: "))
        contador = contador + 1
        if (contador == 2):
            print("tarjeta bloqueada")
            opcion=1
    if (c == 1803):
        mr = int(input("ingrese el monto que desea retirar: "))
        if (mr > 100000):
            print("monto no permitido")
        else:
            print("usted a retirado $", mr)
            print("saldo cuenta: ", sui - mr)
            print("saldo cajero: ", sci - mr)
    sui = sui - mr
    sci = sci - mr
    opcion=int(input("desea continuar? N:1, S:0 "))
if(opcion==1):
  print("adiós")