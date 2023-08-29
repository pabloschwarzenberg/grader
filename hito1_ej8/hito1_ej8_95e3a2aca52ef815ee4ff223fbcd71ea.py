#Descomponer un número
numero=str(input(""))
if len(numero)==4:
    unidades=int(numero[-1])
    decenas=int(numero[-2])
    centenas=int(numero[-3])
    miles=int(numero[-4])
    print(miles,"M +", centenas,"C +", decenas,"D +", unidades,"U")
if len(numero)==3:
    unidades=int(numero[-1])
    decenas=int(numero[-2])
    centenas=int(numero[-3])
    print(centenas,"C +", decenas,"D +", unidades,"U")
if len(numero)==2:
    unidades=int(numero[-1])
    decenas=int(numero[-2])
    print(decenas, "D +", unidades, "U")
if len(numero)==1:
    unidades=numero
    print(unidades, "U")
