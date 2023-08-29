#Descomponer un número
num = input("ingrese un numero de max. 4 digitos: ")
if len(num) == 1:
    print("{}U".format(num))
elif len(num) == 2:
    a = num[0:1]
    b = num[1:2]
    print("{}D + {}U".format(a, b))
elif len(num) == 3:
    a = num[0:1]
    b = num[1:2]
    c = num[2:3]
    print("{}C + {}D + {}U".format(a, b, c))
elif len(num) == 4:
    a = num[0:1]
    b = num[1:2]
    c = num[2:3]
    d = num[3:4]
    print("{}M + {}C + {}D + {}U".format(a, b, c, d))