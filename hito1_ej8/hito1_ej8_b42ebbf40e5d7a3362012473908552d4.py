#Descomponer un número
a = str(input("Ingrese un numero de hasta 4 digitos"))
b = int(a)

if b < 10:
    print(a+"U")
elif b > 10 and b < 100:
    print(a[0]+"D + "+a[1]+"U")
elif b >= 100 and b < 1000:
    print(a[0]+"C + "+a[1]+"D + "+a[2]+"U")
elif b >= 1000 and b < 10000:
    print(a[0]+"M + "+a[1]+"C + "+a[2]+"D + "+a[3]+"U")     