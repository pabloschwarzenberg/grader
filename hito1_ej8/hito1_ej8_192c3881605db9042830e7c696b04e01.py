#Descomponer un número
if umil<=0:
    print(centenas, "C + ",decenas, "D +", unidades, "U")
    if centenas<=0:
        print(decenas, "D +", unidades, "U")
        if decenas<0:
            print(unidades, "U")