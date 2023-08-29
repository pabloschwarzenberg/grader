#Juego adivina mi número
n = 7
i = 0
while i<5:
  a = int(input("Elige un número entre el 1 y el 20: "))
  if a != n:
    if a>n:
      print("mi numero es menor")
      i+=1
    elif a<n:
      print("mi numero es mayor")
      i+=1
  else:
    print("Adivinaste, mi numero era",n)
    break
print("No adivinaste, mi nuero era",n)
      