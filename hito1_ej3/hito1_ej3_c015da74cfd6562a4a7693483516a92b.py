#Aprobación de créditos
ingreso=int(input("Ingreso:"))
anoNacimiento=int(input("Ano de nacimiento"))
numeroHijos=int(input("Numero de hijos:"))
anosPertenencia=int(input("Anos de pertenencia al banco:"))
estadoCivil=input("Estado civil S o C:")
vive=input("Campo o ciudad U o R:")

if anosPertenencia>10 and numeroHijos>=2:
    print("APROBADO")

elif estadoCivil=="S" and numeroHijos>3 and 45<=(2020-anoNacimiento)<=55:
    print("APROBADO")

elif ingreso>2500000 and estadoCivil=="S" and vive=="U":
    print("APROBADO")

elif anosPertenencia>5 and ingreso>3500000:
    print("APROBADO")

elif vive=="R" and estadoCivil=="C" and numeroHijos<2:
    print("APROBADO")

else:
    print("RECHAZADO")

    
      