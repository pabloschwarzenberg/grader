#Cajero Automático
  CLAVE = input("ingrese clave: ")
Montoinicial = 1000000   

Saldo = 100000

n=1

while  (CLAVE == "1803" and (n < 4)):

   

    MONTORETIRAR = eval(input("ingresar monto a retirar? "))

  

    if MONTORETIRAR >= 100000:

      

      print("“monto no permitido”")

      import sys

      sys.exit()

 

    else:

            

       print("“monto permitido”")

 

       Saldofinal = Saldo - MONTORETIRAR

       print("Saldo Cuenta = ",Saldofinal)

 

       Saldocajero = Montoinicial - MONTORETIRAR

       print("Saldo Cajero = ",Saldocajero)

       import sys

       sys.exit()

       

else:

        print("Clave invalida")

        print("n: ",n)
    
      