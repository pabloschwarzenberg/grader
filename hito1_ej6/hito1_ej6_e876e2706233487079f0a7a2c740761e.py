#Ordenar tres números
print("ingrese tres numeros enteros")
num1=input("Primer Numero:")
num2=input("Segundo Numero:")
num3=input("Tercer Numero:")

if num1<=num3 and num1<=num2:
  if num2<=num3:
    print(num1," , ",num2," , ",num3)
  if num3<=num2:
    print(num1," , ",num3," , ",num2)
if num2<=num3 and num2<=num1:
   if num1<=num3:
    print(num2," , ",num1," , ",num3)
if num3<=num1:
    print(num2," , ",num3," , ",num1)
if num3<=num1 and num3<=num2:
  if num2<=num1:
    print(num3," , ",num2," , ",num1)
  if num1<=num2:
    print(num3," , ",num1," , ",num3)



