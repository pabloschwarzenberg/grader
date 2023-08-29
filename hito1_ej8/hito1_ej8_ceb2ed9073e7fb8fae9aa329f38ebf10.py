#Descomponer un número
n = int(input("Ingrese un numero :"))
if len(str(n)) > 4 :
    while len(str(n)) > 4 :
        n = int(input("Ingrese un numero :"))
if len(str(n)) == 4 :
    print(str(n)[0],"M +",str(n)[1],"C +", str(n)[2], "D +", str(n)[3], "U")
elif len(str(n)) == 3 :
    print(str(n)[0],"C +", str(n)[1], "D +", str(n)[2], "U")
elif len(str(n)) == 2 :
    print(str(n)[0], "D +", str(n)[1], "U")
elif len(str(n)) == 1 :
    print(n,"U")