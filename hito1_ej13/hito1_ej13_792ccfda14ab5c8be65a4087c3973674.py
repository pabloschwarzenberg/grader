x = int(2)
n = int(input("Ingrese un numero: "))
while n != 1:
    if n % x == 0:
        print(str(x) + "")
        n = n /x
    else:
        x = x + 1