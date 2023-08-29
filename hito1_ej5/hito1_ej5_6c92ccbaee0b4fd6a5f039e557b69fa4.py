#Cálculo del dígito verificador de un rut
Rut = str(input("Ingrese su RUT sin digito verificador: "))
DigitoVerificador = int(0)
A = int(2)
B = int(len(Rut))
C = int(B - 1)
D = int(B)
E = int(1)
Suma = int(0)
while B != 0:
    N = int(Rut[C:D])
    Multiplicacion = N * A
    if E == 1:
        Suma = Multiplicacion
        E = 0
        A = A + 1
    elif A == 7:
        A = 2
        Suma = Suma + Multiplicacion
    else:
        A = A + 1
        Suma = Suma + Multiplicacion
    B = B - 1
    C = C - 1
    D = D - 1
Resto = Suma % 11
DigitoVerificador = 11 - Resto
if DigitoVerificador == 10:
    DigitoVerificador = "K"
elif DigitoVerificador == 11:
    DigitoVerificador = 0
else:
    DigitoVerificador = DigitoVerificador
print("Dv=",DigitoVerificador)