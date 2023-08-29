#Cálculo del dígito verificador de un rut
rut = int(input("ingrese su rut: "))

Rut = str(rut)
lista = Rut.split()

suma = [0]*2 + [1]*3 + [2]*4 + [3]*5 + [4]*6 + [5]*7 + [6]*2 + [7]*3

if len(lista) == 7 and digit <10:
    digit = suma%11
    print("dv =", digit)
elif len(lista) == 7 and digit == 11:
    print("dv = 0")
elif len(lista) == 7 and digit == 10:
    print("dv = k")
else:
    print("codigo incorrecto")
