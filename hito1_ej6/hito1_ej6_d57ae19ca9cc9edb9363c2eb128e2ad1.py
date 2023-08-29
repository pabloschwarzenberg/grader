numero1 = int(input("Primer Numero:",))
numero2 = int(input("Segundo Numero:",))
numero3 = int(input("Tercer Numero:",))
if numero1 <= numero2 and numero1 <= numero3:
 if numero2 <= numero3:
   print (numero1,",",numero2,",",numero3)
 if numero3 <= numero2:
   print (numero1,",",numero3,",",numero2)
if numero2 <= numero1 and numero2 <= numero3:
 if numero1 <= numero3:
   print (numero2,",",numero1,",",numero3)
 if numero3 <= numero1:
   print (numero2,",",numero3,",",numero1)
if numero3 <= numero2 and numero3 <= numero1:
 if numero2 <= numero1:
   print (numero3,",",numero2,",",numero1)
 if numero1 <= numero2:
   print (numero3,",",numero1,",",numero2)