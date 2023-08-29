num = int (input("Ingrese un número"))
factor = 2


while factor <= num:
    if not (num % factor != 0):
        print(factor)
        num /= factor
    else:
        factor +=1
