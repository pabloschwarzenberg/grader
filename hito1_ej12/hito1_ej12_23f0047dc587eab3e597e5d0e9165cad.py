import random     
numero = random.randint(1, 20)
intentos=0
i = []
while intentos<5:
    estimacion=int(input())#"Intenta adivinar:"
    intentos=intentos + 1
    i.append(estimacion)
    if estimacion<numero:
      print("mi número es menor")
    if estimacion>numero:
      print("mi número es mayor")
    if estimacion==numero:
      break
    if len(i) == 5 and estimacion != numero :
      raise NameError("{0}".format(i))
      
if estimacion==numero:
  numero=str(numero)
  print("Adivinaste, mi numero era " + numero)
  
elif estimacion!=numero:
  numero=str(numero)
  print("No adivinaste, mi numero era " + numero)






