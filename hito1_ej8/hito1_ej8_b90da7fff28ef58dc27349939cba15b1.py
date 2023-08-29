#Descomponer un número
x=input("Ingrese un numero de 4 digitos")
y=len(x)

if y==4:
    a = x[0]
    b = x[1]
    c = x[2]
    d = x[3]
    print("{}M + {}C + {}D + {}U".format(a, b, c, d))
if y==3:
    a = x[0]
    b = x[1]
    c = x[2]
    print("{}C + {}D + {}U".format(a, b, c))
if y==2:
    a = x[0]
    b = x[1]
    print("{}D + {}U".format(a, b))
if y==1:
    a = x[0]
    print("{}U".format(a))