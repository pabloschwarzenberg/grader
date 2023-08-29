#Descomponer un número
x = str(input("ingrese un numero entero: "))
if (int(x) / 1000) >= 1 and (int(x) / 100) < 1000:
    print("Para: ", x, "debe imprimri: ", x[0], "M +", x[1], "C +", x[2], "D +", x[3], "U")

elif (int(x) / 100) >= 1 and (int(x) / 100) < 100:
    print("Para: ", x, "debe imprimri: ", x[0], "C +", x[1], "D +", x[2], "U")

elif (int(x) / 10) >= 1 and (int(x) / 100) < 10:
    print("Para: ", x, "debe imprimri: ", x[0], "D +", x[1], "U")

elif (int(x) / 10) <= 1:
    print("Para: ", x, "debe imprimri: ", x[0], "U")


    

