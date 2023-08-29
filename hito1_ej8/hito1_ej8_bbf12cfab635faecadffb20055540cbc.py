x = str(input("Inserte el numero de max 4 digitos: "))
if len(x) == 4:
    subcadena1 = int(x[-1])
    subcadena2 = int(x[-2])
    subcadena3 = int(x[-3])
    subcadena4 = int(x[-4])
    print(subcadena4,"M+", subcadena3,"C+",subcadena2,"D+", subcadena1,"U+")
if len(x) == 3:
    subcadena1 = int(x[-1])
    subcadena2 = int(x[-2])
    subcadena3 = int(x[-3])
    print(subcadena3, "C+",subcadena2,"D+",subcadena1,"U+")
if len(x) == 2:
    subcadena1 = int(x[-1])
    subcadena2 = int(x[-2])
    print(subcadena2, "D+", subcadena1, "U+")
if len(x) == 1:
    print(x,"U")