#Factores Primos
x = int(2)
N = int(input("Ingrese cualquier numero -> "))

while(N != 1):
    if (N % x == 0 ):
        print(str(x) + "")
        N = N / x
    else:
        x = x + 1 