#Ordenar tres números
num1=eval(input("Ingrese su primer numero:"))
num2=eval(input("Ingrese su segundo numero:"))
num3=eval(input("Ingrese su tercer numero:"))

NMAYOR=max(num1,num2,num3)
NMENOR=min(num1,num2,num3)
MEDIO=(num1 + num2 + num3) - NMAYOR - NMENOR
print(NMENOR ,",", MEDIO,",", NMAYOR ,)