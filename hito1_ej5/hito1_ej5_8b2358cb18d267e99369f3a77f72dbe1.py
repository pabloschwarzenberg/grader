Rut = int(input("Ingresa tu RUT, sin puntos y sin el nÃºmero verificador: "))

Digito1 = Rut//10000000
sobrante1 = Rut%10000000

Digito2 = sobrante1//1000000
sobrante2 = Rut%1000000

Digito3 = sobrante2//100000
sobrante3 = Rut%100000

Digito4 = sobrante3//10000
sobrante4 = Rut%10000

Digito5 = sobrante4//1000
sobrante5 = Rut%1000

Digito6 = sobrante5//100
sobrante6 = Rut%100

Digito7 = sobrante6//10
sobrante7 = Rut%10

Digito8 = sobrante7//1

Suma = Digito8*2 + Digito7*3 + Digito6*4 + Digito5*5 + Digito4*6 + Digito3*7 + Digito2*2 + Digito1*3

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