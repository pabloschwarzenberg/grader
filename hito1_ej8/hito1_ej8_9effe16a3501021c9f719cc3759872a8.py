a = int(input(" porfavor ingrese un número de un maximo de 4 digitos:"))
while len(str(a)) > 4 or a < 1:
 a = int(input("porfavor ingrese un número de un maximo de 4 digitos:"))
sa = str(a)
if len(str(a)) == 1:
    print(sa[0] + "U")
elif len(str(a)) == 2:
    print(sa[0] + "D + " + sa[1] + "U")
elif len(str(a)) == 3:
    print(sa[0] + "C + " + sa[1] + "D + " + sa[2] + "U")
elif len(str(a)) == 4:
    print(sa[0] + "M + " + sa[1] + "C + " + sa[2] + "D + " + sa[3] + "U")