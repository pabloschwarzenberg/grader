#Descomponer un número
N = eval(input("Ingrese un numero de hasta 4 digitos: "))

a = (N // 1000) % 10
b = (N // 100) % 10
c = (N // 10) % 10
d = (N // 1) % 10

if (N < 10):
    print(d, "U")
elif (10 <= N < 100):
    print(c, "D+", d, "U")
elif (100 <= N < 1000):
    print(b, "C+", c, "D+", d, "U")
elif (1000 <= N < 10000):
    print(a, "M+", b, "C+", c, "D+", d, "U")