#Cajero Automático
saldo_cajero = 1000000
saldo_cuenta = 100000
usuario = 10334151
clave = 1803
usuario = int(input("Ingrese numero de usuario:"))
if usuario == 10334151:
 i = 1
 while i<=3:
           validar_clave = int(input("Ingrese su clave por favor:"))
           if(validar_clave != 1803):
                print("clave invalida")
                i = i + 1
                if(i == 3):
                     print("tarjeta bloqueada")
                     break
           else:
               monto = int(input("Cual es el monto que desea retirar"))
               if(monto>saldo_cuenta):
                     print("Monto no permitido")
               else:
                   saldo_cuenta = saldo_cuenta - monto
                   saldo_cajero = saldo_cajero - monto
                   print("saldo cuenta=",saldo_cuenta)
                   print("saldo cajero=",saldo_cajero)
                   continuar = input("Pulse N si desea continuar, pulse otra tecla si desea salir:")
                   if (continuar != "N"):
                       break
                  
               
               
       
       