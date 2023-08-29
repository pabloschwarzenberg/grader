import random 
nro_secreto = random.randint(1,20)
error = 0
while error < 5:
  adivinacion = int(input("Adivina mi numero: "))
  if adivinacion != nro_secreto:
    error += 1
  if adivinacion != nro_secreto:  
    if adivinacion < nro_secreto and error != 5:
      print("mi número es mayor")
    if adivinacion > nro_secreto:
      print("mi número es menor")
    
  if adivinacion == nro_secreto:
    print("Adivinaste, mi número era "+str(adivinacion))
    break
if error >= 5:
  print("No adivinaste, mi número era "+str(nro_secreto))