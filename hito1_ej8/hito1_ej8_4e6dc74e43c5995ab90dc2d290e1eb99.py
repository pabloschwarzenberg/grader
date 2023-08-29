#Descomponer un número
#variable
N = input("Ingrese un numero: ")

try:
    N = int(N)
    if 1000 <= N <= 9999:
        N = str(N)
        print(N[0] + "M", "+", N[1] + "C", "+", N[2] + "D", "+", N[3] + "U")
    elif 100 <= N <= 999:
        N = str(N)
        print(N[0] + "C", "+", N[1] + "D", "+", N[2] + "U")
    elif 10 <= N <= 99:
        N = str(N)
        print(N[0] + "D", "+", N[1] + "U")
    elif 0 <= N <= 9:
        N = str(N)
        print(N[0] + "U")
except ValueError:
    print("No es un numero.")   