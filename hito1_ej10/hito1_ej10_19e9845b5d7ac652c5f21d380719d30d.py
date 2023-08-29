 #Cajero Automatico
from time import sleep 
saldo_cajero=1000000
saldo_usurio=100000
usuario=str(int(input("Ingrese el usuario:")))
contrasena=str (int(input("Ingrese la contraseña:")))
while True :
    if usuario=="10334151" and contrasena == "1803":
        print ("Usuario y contraseña correctos")
    sleep(1)
    monto_a_retirar=int(input("ingrese el monto a retirar:"))
    if monto_a_retirar> saldo_usurio and monto_a_retirar>saldo_cajero:
                           print ("monto no permitido  ")
    break 
        
if monto_a_retirar<saldo_usurio and monto_a_retirar < saldo_cajero:
          saldo_usurio_final =saldo_usurio-monto_a_retirar 
          saldo_cajero_final =saldo_cajero-monto_a_retirar
print("sadldo cuenta=",saldo_usurio_final)
print("saldo cajero=",saldo_cajero_final)

if monto_a_retirar!="N":
                                                       
    if usuario!="10224151"or contrasena!="1803":
            print("calve invalida")
            sleep(1)
            print("intento numero 2")
            sleep(1)
            contrasena=float(int(input("ingrese la contraseña de nuevo:")))
            if usuario!="10224151"or contrasena!="1803":
                      print("calve invalida")
            sleep(1)
            print("intento numero 3")
            sleep(1)
            contrasena=str(int(input("ingrese la contraseña de nuevo:")))
           
            if usuario!="10334151"or contrasena!="1803":
                    print("tarjeta bloqueada ")
                                                           