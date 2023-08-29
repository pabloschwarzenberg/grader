#Ordenar tres números
print("Ingrese un primer número: ")
num1 = int(input())
print("Ingrese un segundo número: ")
num2 = int(input())
print("Ingrese un tercer número: ")
num3 = int(input())
if ((num1 <= num2) and (num1 <= num3)):
    a = num1;
    if (num2 <= num3):
        b = num2;
        c = num3;
    else:
        b = num3;
        c = num2;
elif ((num2 <= num1) and (num2 < num3)):
    a = num2;
    if (num1 <= num3):
        b = num1;
        c = num3;
    else:
        b = num3;
        c = num1;
else:
    a = num3;
    if (num1 <= num2):
        b = num1;
        c = num2;
    else:
        b = num2;
        c = num1;
print(a,",",b,",",c)