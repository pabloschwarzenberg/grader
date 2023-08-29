#Cálculo del dígito verificador de un rut
Rut = int(input("Ingresa tu RUT, sin puntos y sin el numero verificador: "))

D1 = Rut//10000000
sobrante1 = Rut%10000000

D2 = sobrante1//1000000
sobrante2 = Rut%1000000

D3 = sobrante2//100000
sobrante3 = Rut%100000

D4 = sobrante3//10000
sobrante4 = Rut%10000

D5 = sobrante4//1000
sobrante5 = Rut%1000

D6 = sobrante5//100
sobrante6 = Rut%100

D7 = sobrante6//10
sobrante7 = Rut%10

D8 = sobrante7//1

Suma = D8*2 + D7*3 + D6*4 + D5*5 + D4*6 + D3*7 + D2*2 + D1*3

Entero = Suma//11
Resto = Suma-(11*Entero)
Verificador = 11 - Resto
if(Verificador == 11):
    dv=0
elif(Verificador == 10):
    dv="k"
else:
    dv=Verificador
print("dv =",dv)