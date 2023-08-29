#Cálculo del dígito verificador de un rut
rut=str(input("ingrese los digitos de su rut : "))
caracteres=len(rut)
posicion=caracteres-1
rango=range(caracteres)
form=0
for a in rango:
    if a == 6:
        form = form + (int(rut[posicion]) * 2)
        posicion = posicion - 1
    elif a == 7:
        form = form + (int(rut[posicion]) * 3)
        posicion = posicion - 1
    else:
        form = form + (int(rut[posicion])*(a+2))
        posicion = posicion - 1
form=form % 11
form=11-form
if form>=11:
    print("dv=0")
elif form==10:
    print("dv=K")
else:
    print("dv=",form)      