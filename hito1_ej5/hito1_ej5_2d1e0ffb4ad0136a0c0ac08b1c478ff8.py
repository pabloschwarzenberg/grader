#Cálculo del dígito verificador de un rut
print("ingrese su rut")
rut = str(input())

#20.590.499

while(len(rut) > 8) or (len(rut) < 7):
    print("ingrese su rut de nuevo")
    rut = str(input())

if(len(rut) == 8):

    numero1 = rut[7]
    numero2 = rut[6]
    numero3 = rut[5]
    numero4 = rut[4]
    numero5 = rut[3]
    numero6 = rut[2]
    numero7 = rut[1]
    numero8 = rut[0]

    Nnumero1 = int(numero1)
    Nnumero2 = int(numero2)
    Nnumero3 = int(numero3)
    Nnumero4 = int(numero4)
    Nnumero5 = int(numero5)
    Nnumero6 = int(numero6)
    Nnumero7 = int(numero7)
    Nnumero8 = int(numero8)

    cantidad1 = Nnumero1 * 2
    cantidad2 = Nnumero2 * 3
    cantidad3 = Nnumero3 * 4
    cantidad4 = Nnumero4 * 5
    cantidad5 = Nnumero5 * 6
    cantidad6 = Nnumero6 * 7
    cantidad7 = Nnumero7 * 2
    cantidad8 = Nnumero8 * 3

    suma = cantidad1 + cantidad2 + cantidad3 + cantidad4 + cantidad5 + cantidad6 + cantidad7 + cantidad8

    division = suma / 11
    division0 = round(division)

    resto = suma - (11 * division0)
    dv = 11 - resto

    print(dv)