x = 2
num = int(input("Ingresar numero: "))

while (num != 1):
    if ((num % x) == 0):
        print(str(x)+" ")
        num /= x
    else:
        x += 1