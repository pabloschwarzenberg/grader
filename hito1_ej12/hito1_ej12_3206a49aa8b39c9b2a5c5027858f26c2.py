#Juego adivina mi número
num = int(input("Ingrese un número"))
while num != 33:
  if num >= 100:
    num = int(input("Numero equivocado, solo deben ser menores a 100. Ingrese un número"))
  else :
    num = int(input("Numero equivocado, está dentro del rango. Ingrese un número"))

print("Perfecto!!")