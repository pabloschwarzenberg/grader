print("Ordenar numeros de menor a mayor")
numero_1 = int(input("Ingresar el primer numero: "))
numero_2 = int(input("Ingresar el segundo numero: "))
numero_3 = int(input("Ingresar el tercer numero: ")) 
if numero_1 <= numero_2 and numero_1 <= numero_3:
  menor = numero_1
  if numero_2 <= numero_3:
    medio = numero_2 
    mayor = numero_3
  else:
    medio = numero_3
    mayor = numero_2
elif numero_2 <= numero_1 and numero_2 < numero_3:
  menor = numero_2
  if numero_1 <= numero_3:
    medio = numero_1
    mayor = numero_3
  else:
    medio = numero_3
    mayor = numero_1
else:
  menor = numero_3
  if numero_1 <= numero_2:
    medio = numero_1
    mayor = numero_2
  else:
    medio = numero_2
    mayor = numero_1

print(str(menor),",",str(medio),", ",str(mayor))
