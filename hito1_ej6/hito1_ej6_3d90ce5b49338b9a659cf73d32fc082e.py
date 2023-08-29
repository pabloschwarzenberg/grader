#Ordenar tres números
#Ordenar tres números
num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))
num3 = int(input("Ingrese tercer numero: "))
if(num1 <= num2 and num1 <= num3):
    if(num2 <= num3):
        print("Numeros de menor a mayor:", num1,",",num2,",",num3)
    else:
        print("Numeros de menor a mayor:", num1, ",", num3, ",", num2)

if(num2 <= num1 and num2 <= num3):
    if(num1 <= num3):
        print("Numeros de menor a mayor:", num2,",",num1,",",num3)
    else:
        print("Numeros de menor a mayor:", num2, ",", num3, ",", num1)

if(num3 <= num1 and num3 <= num2):
    if(num1 <= num2):
        print("Numeros de menor a mayor:", num3,",",num1,",",num2)
    else:
        print("Numeros de menor a mayor:", num3, ",", num2, ",", num1)
