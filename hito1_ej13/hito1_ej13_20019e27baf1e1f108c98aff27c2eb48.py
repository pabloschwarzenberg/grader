#Factores Primos
x = int(2);
nm = int(input("Ingrese el número a calcular factores primos: "));
while (nm != 1):
    if (nm % x == 0):
        print(str(x)+" ");
        nm = nm / x;
    else:
        x = x + 1;