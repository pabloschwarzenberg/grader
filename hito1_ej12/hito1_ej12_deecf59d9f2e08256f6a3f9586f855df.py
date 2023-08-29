import random

 numero = random.randint(1, 20)

 print ("estoy pensando en un número entre el 1 y el 20.")
 
 while intentosRealizados < 5:
  print ("adivina el numero")
    estimacion = input()
    estimacion = int(estimacion)
  
  intentosRealizados = intentosRealizados + 1
  
  if estimacion < numero:
   print ("mi numero es mayor")
  
  if estimacion > numero:
   print ("mi numero es menor")
  
  if estimacion == numero:
   break
  
 if estimacion == numero:
  intentosRealizados = str (intentosRealizados)
   print ("Adivinaste :D !, mi numero era:" + numero )
  
 if estimacion != numero:
  numero = str (numero)
   print ('No adivinaste :C , mi numero era:' + numero)