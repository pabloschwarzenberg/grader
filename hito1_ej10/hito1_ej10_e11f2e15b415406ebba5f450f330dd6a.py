#Cajero Automático
intento = 3
while intento>0:
   usuario = input("ingrese usuario:  ")
   clave = input("ingrese clave:  ")
   if usuario == "10334151" and clave == "1803":
      print("ingreso correcto")

      sal_cue = 100000
      sal_caj = 1000000
      

      m = int(input("monto a retirar:  "))

      if m <= sal_caj:
         sal_caj = sal_caj - m
         sal_cue = sal_cue - m
                     

         print("Retiro Exitoso!!!")

         print("saldo actual del cajero:",sal_caj)
         print("su saldo actual en la cuenta es:",sal_cue)
         
      elif m <= sal_cue:
         sal_caj = sal_caj - m
         sal_cue = sal_cue - m

   
            

         print("Retiro Exitoso!!!")

         print("saldo actual del cajero:",sal_caj)
         print("su saldo actual en la cuenta es:",sal_cue)


      else: 
         print("MONTO NO VALIDO")
         
      
      
      
      
   else:
      print("usuario o clave no valido")
      intento = intento - 1
   if  intento == 0:
      print("su tarjeta se blokio :v")