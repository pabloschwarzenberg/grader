num=int(input("Introduzca un número: "))
i=2

while i <= num:
    if num % i==0:
        print(i)
        num= num // i

    else:
        i= i + 1