##Descomponer un número

num = input("Escribe un número de máximo cuatro dígitos: ")

vuelta = 0
while vuelta <= len(str(num)):
    dig = int(num)
    dig = dig//(10**vuelta)
    dig = dig%10
    if vuelta == 0:
        U = str(dig)+"U"
    elif vuelta == 1:
        D = str(dig)+"D"
    elif vuelta == 2:
        C = str(dig)+"C"
    elif vuelta == 3:
        M = str(dig)+"M"
    vuelta = vuelta + 1
    
if len(num) == 4:
    print(str(M), str(C), str(D), str(U), sep="+")
elif len(num) == 3:
    print(str(C), str(D), str(U), sep="+")
elif len(num) == 2:
    print(str(D), str(U), sep="+")
elif len(num) == 1:
    print(str(U))