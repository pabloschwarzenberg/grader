#Aprobación de créditos
ingresos= float(input("ingrese sus ingresos"))
año_nacimiento= int(input("ingrese su año de nacimiento:"))
n_hijos= int(input("ingrese la cantidad de hijos que tiene:"))
a_pertenencia= int(input("ingrese cuantos años lleva perteneciendo al banco:"))
e_civil= input("ingrese su estado civil, S: para soltero, C: para casado:")
localizacion= input("ingrese su lugar de vivienda, U: para un lugar urbano, R: para un lugar rural:")
e_civil_casado= str(e_civil)
año_nacimiento += -2021
#desarrollo
if (a_pertenencia) > (10) and (n_hijos) >= (2):
    print("credito aprobado")
elif (e_civil) == (C) and (n_hijos) > (3) and ((año_nacimiento) == [45,46,47,48,49,50,51,52,53,54,55]):
    print("credito aprobado")
elif (ingresos) > (2500000) and (e_civil) == (S) and (localizacion) == (U):
    print("credito aprobado")
elif (ingresos) > (3500000) and (a_pertenencia) > (5):
    print("credito aprobado")
elif (localizacion) == (R) and (e_civil) == (C) and (n_hijos) < (2):
    print("credito aprobado")
else:
    print("credito rechazado")
   