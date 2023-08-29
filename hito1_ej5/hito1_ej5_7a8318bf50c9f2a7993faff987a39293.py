#Cálculo del dígito verificador de un rut
rut=[int(x) for x in input("Ingrese rut sin puntos ni el numero despues del guion: ")]
n=len(rut)
lista = rut
if n == 7:
    suma=lista[n-1]*2+lista[n-2]*3+lista[n-3]*4+lista[n-4]*5+lista[n-5]*6+lista[n-6]*7+lista[n-7]*2
else:
    suma=lista[n-1]*2+lista[n-2]*3+lista[n-3]*4+lista[n-4]*5+lista[n-5]*6+lista[n-6]*7+lista[n-7]*2+lista[n-8]*3
resto=suma%11
dv=11-resto
if dv == 10:
    dv ="k"
    print("dv=",dv)
elif dv == 11:
    dv = 0
    print("dv=",dv)
else:
    print("dv=",dv)
