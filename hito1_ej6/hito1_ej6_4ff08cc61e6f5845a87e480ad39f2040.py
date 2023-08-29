#Ordenar tres números
num1=int(input("Ingrese su primer número: "))
num2=int(input("Ingrese su segundo número: "))
num3=int(input("Ingrese su tercer número: "))
menor,medio,mayor= 0,0,0
if num1 > num2 and num1 > num3:
  mayor= num1
  if num2 > num3:
   medio,menor= num2,num3
  else:
    medio,menor= num3,num2
elif num2 > num1 and num2 > num3:
  mayor= num2
  if num1 > num3:
   medio,menor= num1,num3
  else:
    medio,menor= num3,num1
else:
  num3 > num2 and num3 > num1
  mayor= num3
  if num2 > num1:
   medio,menor= num2,num1
  else:
   medio,menor= num1,num2 
print("Los numeros ordenados de menor a mayor son:",menor,",",medio,",",mayor)    