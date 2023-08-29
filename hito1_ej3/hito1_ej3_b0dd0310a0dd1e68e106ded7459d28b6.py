#Aprobación de créditos
print("Estimado usuario, por favor ingrese los datos solicitados para procesar su crédito")
ingreso=int(input("Escriba su ingreso mensual: $ "))
print("Escriba su fecha de nacimiento")
amo=int(input("Año: "))
hijos=int(input("Escriba el número de hijos que tiene: "))
pertenencia=int(input("Escriba los años de pertenencia al banco: "))
estadocivil=input("Escriba su estado civil; C si es casado, S si es soltero: ")
while not (estadocivil=="C" or estadocivil=="S"):
    print("Estado civil incorrecto. Inténtelo de nuevo")
    estadocivil=input("Escriba su estado civil; C si es casado, S si es soltero: ")
vivencia=input("Escriba dónde está su residencia; U si es urbano, R si es rural: ")
while not(vivencia=="U" or vivencia=="R"):
    print("Residencia mal ingresada. Inténtelo de nuevo")
    vivencia==input("Escriba dónde está su residencia; U si es urbano, R si es rural: ")
if pertenencia>10 and hijos>=2:
    print("APROBADO")
elif estadocivil=="C" and hijos>3 and 1952<=amo<=1962:
    print("APROBADO")
elif ingreso>2500000 and estadocivil=="S" and vivencia=="U":
    print("APROBADO")
elif ingreso>3500000 and pertenecia>5:
    print("APROBADO")
elif vivencia=="R" and estadocivil=="C"and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
          