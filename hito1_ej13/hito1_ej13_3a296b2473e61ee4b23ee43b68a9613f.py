num=int(input("Introduzca un número: "))
x=2
while x <= num:
    if num % x==0:
        print(x)
        num= num // x
    else:
        x= x + 1