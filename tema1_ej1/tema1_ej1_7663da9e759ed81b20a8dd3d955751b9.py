#Suma de los N primeros números
num= int(input("Ingrese un número: "))
cont= 1
while num >= cont:
  res= cont*(cont + 1)/2
  print("suma",int(res))
  cont= cont + 1