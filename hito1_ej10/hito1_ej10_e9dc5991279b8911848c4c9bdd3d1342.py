#Cajero Automático
 ciclo=0
ciclomaestro=0
saldo=100000
contador=0
cajero=1000000

while(ciclomaestro==0):
   
    input("usuario: ")
    while(ciclo==0):
         clave=int(input("clave: "))
         if clave==1803:
            ciclo=2
         else:
            contador=contador+1
         if contador==3:
            ciclomaestro=1
            ciclo=1
            print("Su tarjeta a sido bloqueada")
            

    while(ciclo==2):
       p=int(input("Quiere hacer un retiro?\n[1].SI\n[2].NO\n.........."))
       if p==1:
           cantidad=int(input("Cuanto quiere retirar: "))
           if cantidad<saldo:
               saldo=saldo-cantidad
               cajero=cajero-cantidad
               print(f"saldo cuenta={saldo}\nsaldo cajero={cajero}")
               ciclo=0
               salir=input("Para salir ingrese algo distinto de n: ")
               if salir!="n":
                   ciclomaestro=1
           else:
               print("Saldo insuficiente\n")
       else:
           salir=input("Para salir ingrese algo distinto de n: ")
           if salir!="n":
              ciclomaestro=1
           else:
               ciclo=0


