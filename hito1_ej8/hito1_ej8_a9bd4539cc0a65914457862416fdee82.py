#Descomponer un número
x = int(input("ingrese un numero de maximo 4 digitos: "))
x = str(x)
if len(str(x))==4:
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    print(x1+"M +" ,x2+"C +" ,x3+"D +" ,x4+"U")
else:
    if len(str(x))==3:
        x1 = x[0]
        x2 = x[1]
        x3 = x[2]
        print(x1+"C +" ,x2+"D +" ,x3+"U")
    else:
        if len(str(x))==2:
            x1 = x[0]
            x2 = x[1]
            print(x1 + "D +", x2 + "U")
        else:
            x1 = x[0]
            print(x1 + "U")