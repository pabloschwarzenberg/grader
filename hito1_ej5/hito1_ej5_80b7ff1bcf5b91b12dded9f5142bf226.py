#Cálculo del dígito verificador de un rut
rut=int(input("Ingresa RUT"))
mult=2
suma=0

while rut!=0:
    ultimo=rut%10
    suma=suma+ultimo*mult

    mult=mult+1
    if mult==8:
        mult=2
    rut=rut//10

resto=suma%11
digito=11-resto
if digito==10:
    print("dv=k")
elif digito==11:
    print("dv=0")
else:
    print("dv=",digito)