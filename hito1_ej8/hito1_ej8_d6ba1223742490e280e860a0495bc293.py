#Descomponer un número
n = int(input("Ingrese un numero de  hasta 4 cifras:"))
while not(n >= n and n <= 9999 ):
    n = int(input("Ingrese un numero de 4 cifras:"))

nStr = str(n)

if(len(nStr) == 4):
    print(nStr[0]+"M + "+ nStr[1] + "C + " + nStr[2] + "D + " + nStr[3] + "U")
if(len(nStr) == 3):
    print(nStr[0] + "C + " + nStr[1] + "D + " + nStr[2] + "U")
if(len(nStr) == 2):
    print(nStr[0] + "D + " + nStr[1] + "U")
if(len(nStr) == 1):
    print(nStr[0] + "U")


