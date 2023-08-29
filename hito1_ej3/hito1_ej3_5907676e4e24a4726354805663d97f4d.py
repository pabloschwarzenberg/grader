#Aprobación de créditos
year = 2020
i = eval(input("ingrese ingresos en pesos: "))
h = eval(input("ingrese cantidad de hijos: "))
n = eval(input("ingrese año de nacimiento: "))
f = eval(input("ingrese años de afiliacion con el banco: "))
e = ord(input("ingrese estado civil (S) soltero (C) casado: "))
v = ord(input("ingrese vivienda (R) rural (U) urbano: "))
a = year - n

if f>10 and h>=2:
    print("APROBADO")
if e==99 and h>3 and a>=45 and a<=55:
    print("APROBADO")
if i>2500000 and e==115 and v==117:
    print("APROBADO")
if i>3500000 and f>5:
    print("APROBADO")
if v==114 and e==99 and h<2:
    print("APROBADO")