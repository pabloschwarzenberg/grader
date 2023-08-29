#Descomponer un númeronumero= int(input("Ingresa un numero de hasta 4 cifras: "))
numero= int(input("Ingresa un numero de hasta 4 cifras: "))

respaldo = numero

d1 = numero%10
numero = numero//10

d2 = numero%10
numero = numero//10

d3 = numero%10
numero = numero//10

d4 = numero%10

if 1<=respaldo<=9:
    CadenaDeCaracteres = str(d1) + "U" 
    print(CadenaDeCaracteres)

elif 10<=respaldo<=99:
    CadenaDeCaracteres2 = str(d2) + "D + "  +  str(d1) + "U" 
    print(CadenaDeCaracteres2)

elif 100<=respaldo<=999:
    CadenaDeCaracteres3 = str(d3) + "C + " + str(d2) + "D + " + str(d1) + "U"
    print(CadenaDeCaracteres3)

elif 1000<=respaldo<=9999:
    CadenaDeCaracteres4 = str(d4) + "M + " + str(d3) + "C + " + str(d2) + "D + " + str(d1) + "U"
    print(CadenaDeCaracteres4)