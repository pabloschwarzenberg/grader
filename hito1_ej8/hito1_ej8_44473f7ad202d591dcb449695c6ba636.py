#Descomponer un número
n = input("Ingrese el número (máx. 4 digitos):")
if len(n) >= 1 or len(n) <= 4:
    x = str(n)
    if len(str(n)) == 1:
        print(x[0] + "U")
    if len(str(n)) == 2:
        print(x[0] + "D +", x[1] + "U")
    if len(str(n)) == 3:
        print(x[0] + "C +", x[1] + "D +", x[2] + "U")
    if len(str(n)) == 4:
        print(x[0] + "M +", x[1] + "C +", x[2] + "D +", x[3] + "U")