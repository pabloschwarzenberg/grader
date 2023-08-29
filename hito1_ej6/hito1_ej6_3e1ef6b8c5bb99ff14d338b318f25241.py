#Ordenar tres números
print("Bienvenido al programa de numeros menor a mayor ")
a = int(input("ingrese un numero "))
b = int(input("ingrese un numero "))
c = int(input("ingrese un numero "))

if ((a <= b) and (a <= c)):
    menor = a
    if (b <= c):
        medio = b;
        mayor = c;
    else:
        medio = c;
        mayor = b;
elif ((b <= c) and (b < c)):
    menor = b;
    if (a <= c):
        medio = a;
        mayor = c;
    else:
        medio = c;
        mayor = a;

else:
    menor = c;
    if (a <= b):
        medio = a;
        mayor = b;
    else:
        medio = b;
        mayor = a;

print("{}, {}, {}".format(menor,medio,mayor))
    