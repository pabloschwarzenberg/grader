#Aprobación de créditos
ingreso=float(input("Ingreso: "))
a=ingreso
año_de_nacimiento=int(input("Año de nacimiento: "))
b=año_de_nacimiento
numero_de_hijos=int(input("Número de hijos: "))
c=numero_de_hijos
años_de_pertenencia_al_banco=int(input("Años de pertenencia la banco: "))
d=años_de_pertenencia_al_banco
estado_civil=input("Estado Civil: ")
e=True
residencia=input("Residencia: ")
f=True
if 10<d and 2<=c or estado_civil=="C" and 3<c and 1972<=b<=1982 or 2500000<a and estado_civil=="S" and residencia=="U" or 3500000<a and 5<d or residencia=="R" and estado_civil=="C" and c<2:
    print("APROBADO")
else:
    print("RECHAZADO")