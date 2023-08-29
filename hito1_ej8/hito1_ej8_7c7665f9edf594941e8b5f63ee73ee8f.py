num=input("Ingrese número de hasta 4 dígitos: ")

x = [int(x) for x in reversed(num)]
if len(x)==1:
    print(x[0], "U")
if len(x)==2:
    print(x[1], "D +",x[0], "U ")
if len(x)==3:
    print(x[2], "C +", x[1], "D +", x[0], "U" )
if len(x)==4:
    print(x[3], "M +",x[2], "C +", x[1],"D +", x[0], "U ")
