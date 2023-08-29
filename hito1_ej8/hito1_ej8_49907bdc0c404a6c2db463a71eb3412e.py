#Descomponer un número
a = int(input("Ingrese un número de hasta 4 digitos:"))
while len(str(a)) > 4 or a < 1:
    a = int(input("Ingrese un número de hasta 4 digitos:"))
sa = str(a)
if len(str(a)) == 1:
    print(sa[0] + "u")
elif len(str(a)) == 2:
    print(sa[0] + "d + " + sa[1] + "u")
elif len(str(a)) == 3:
    print(sa[0] + "c + " + sa[1] + "d + " + sa[2] + "u")
elif len(str(a)) == 4:
    print(sa[0] + "m + " + sa[1] + "c + " + sa[2] + "d + " + sa[3] + "u")