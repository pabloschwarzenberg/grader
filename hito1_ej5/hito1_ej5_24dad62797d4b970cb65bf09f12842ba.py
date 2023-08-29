#Cálculo del dígito verificador de un rut
Rut = int(input("digite su rut sin digito verificador"))
RutAux = str(Rut)
RutAux = RutAux[::-1]
Rut = int(RutAux)
DigitoVerificador = 0
Contador = 1
Suma = 0


for i in RutAux:
    Contador = Contador+1
    if Contador == 8:
        Contador = 2
    DigitoVerificador = int(i)*Contador
    Suma = Suma+DigitoVerificador

Suma = Suma % 11
Suma  = 11 - Suma
Valor = Suma

if Valor == 10:
    Valor = "K"
elif Valor == 11:
    Valor = 0
print("dv","=",Valor)
