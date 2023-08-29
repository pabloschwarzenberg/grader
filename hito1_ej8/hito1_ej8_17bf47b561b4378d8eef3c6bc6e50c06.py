print("Descomponer")
A = int(input("Ingrese un numero de 2 o 4 cifras: "))
C4 = A % 10
C3 = int((A % 100) / 10)
C2 = int((A % 1000) / 100)
C1 = int((A - (A % 1000)) / 1000)
CM = "M"
CC = "C"
CD = "D"
CU = "U"

if A < 100:
    print("Separado es: {}D+{}U".format(C3,C4))
elif A < 1000:
    print("Separado es: {}C+{}D+{}U".format(C2,C3,C4))
elif A < 10000:
    print("Separado es: {}M+{}C+{}D+{}U".format(C1,C2,C3,C4))
else:
    print("El numero ingresado no es valido")

    