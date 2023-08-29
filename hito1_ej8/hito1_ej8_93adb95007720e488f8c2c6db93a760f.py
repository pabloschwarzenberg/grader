#Descomponer un número
x = int(input("Ingrese un número de un maximo de 4 digitos: "))
while len(str(x)) > 4 or x < 1:
    x = int(input("Ingrese un número de un maximo de 4 digitos : "))
sa = str(x)
if len(str(x)) == 1:
    print(sa[0] + "U")
elif len(str(x)) == 2:
    print(sa[0] + "D + " + sa[1] + "U")
elif len(str(x)) == 3:
    print(sa[0] + "C + " + sa[1] + "D + " + sa[2] + "U")
elif len(str(x)) == 4:
    print(sa[0] + "M + " + sa[1] + "C + " + sa[2] + "D + " + sa[3] + "U")     