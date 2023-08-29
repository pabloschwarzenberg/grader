#Ordenar tres números
num1= int(input("Ingrese un número: "))
num2= int(input("Ingrese un número: "))
num3= int(input("Ingrese un número: "))

mayor, medio, menor= 0,0,0
if num1>num2 and num1>num3:
    mayor=num1
    if num2>num3:
        medio,menor=num2,num3
    else:
        medio,menor=num3,num2
elif num2>num1 and num2>num3:
    mayor=num2
    if num1>num3:
        medio,menor=num1,num3
    else:
        medio,menor=num3,num1

else:
    mayor=num3
    if num1>num2:
        medio,menor=num1,num2
    else:
        medio,menor=num2,num1

print(menor,',',medio,',',mayor)

      