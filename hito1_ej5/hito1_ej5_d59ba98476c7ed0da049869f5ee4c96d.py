#Cálculo del dígito verificador de un rut
rut = int(input("Ingresa tu RUT, sin puntos y sin el número verificador: "))

dig1 = rut//10000000
sobrante1 = rut%10000000

dig2 = sobrante1//1000000
sobrante2 = rut%1000000

dig3 = sobrante2//100000
sobrante3 = rut%100000

dig4 = sobrante3//10000
sobrante4 =rut%10000

dig5 = sobrante4//1000
sobrante5 = rut%1000

dig6 = sobrante5//100
sobrante6 = rut%100

dig7 = sobrante6//10
sobrante7 = rut%10

dig8 = sobrante7//1

suma=dig8*2+dig7*3+dig6*4+dig5*5+dig4*6+dig3*7+dig2*2+dig1*3

entero=suma//11
resto=suma-(11*entero)
verif=11-resto
if(verif==11):
    dv=0
elif(verif==10):
    dv="k"
else:
    dv=verif
print("dv =",dv)