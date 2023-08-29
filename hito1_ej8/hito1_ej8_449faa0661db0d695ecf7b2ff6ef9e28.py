num = input("Ingrese un numero hasta 4 cifras: ")

if len(num) == 1:
    print("Para",num, "debe imprimir:", num[0], "U")
if len(num) == 2:
    print("Para",num, "debe imprimir:", num[0], "D +", num[1], "U")
if len(num) == 3:
    print("Para",num, "debe imprimir:", num[0],"C +", num[1], "D +", num[2], "U")   
if len(num) == 4:
    print("Para",num, "debe imprimir:", num[0], "M +", num[1],"C +", num[2], "D +", num[3], "U")