#Ordenar tres números
num1 = int(input("Ingrese numero 1:"))
num2 = int(input("Ingrese numero 2:"))
num3 = int(input("Ingrese numero 3:"))

if ((num1 <= num2) and (num1 <= num3)):
    menor = num1
    if (num2 <= num3):
        medio = num2;
        mayor = num3;
    else:
        medio = num3;
        mayor = num2
elif ((num2 <= num1) and (num2 <= num3)):
    menor = num2
    if (num1 <= num3):
        medio = num1;
        mayor = num3;
    else:
        medio = num3
        mayor = num1
else:
    menor = num3
    if (num1 <= num2):
        medio = num1
        mayor = num2
    else:
        medio = num2
        mayor = num1
print("Los numeros ordenados de menor a mayor son:", menor,",",medio,",",mayor)