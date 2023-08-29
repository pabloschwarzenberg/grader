#Aprobación de créditos
ingreso=int(input("Escriba su ingreso mensual: "))
nacimiento=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("Numero de hijos: "))
anos_pertenencia=int(input("Años con el banco: "))
civil=str(input("Estado civil S o C: "))
lugar=str(input("Campo (R) o Ciudad (U): "))

codigo_civil = ord(civil)

codigo_lugar = ord(lugar) 

edad = 2021-nacimiento

if ((anos_pertenencia>10 and hijos>= 2) or (hijos>3 and 45<edad<55)or(ingreso>2500000 and civil==115 and lugar==117)or(ingreso>3500000 and anos_pertenencia>5)or(lugar==114 and civil==99 and hijos<2)):
    print("APROBADO")
else:
    print("NO APROBADO")      