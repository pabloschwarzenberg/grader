#Aprobación de créditos

ingresos=eval(input("sus ingresos en pesos"))
agno=eval(input("ingrese su año de nacimiento"))
hijos=eval(input("ingrese la cantidad de hijos"))
agnop=eval(input("ingrese sus años de pertencia en el banco"))
estadocivil = input("(S:soltero,C:casado): ")
lugar= input("(U:urbano,R:rural): ")



if agnop>=10 and hijos>=2:
    print("APROBADO")
elif estadocivil=="C" and hijos>=3 and agno>= 1965 and agno<=1975:
    print("APROBADO")
elif ingresos>=2500000 and estadocivil=="S" and lugar=="U":
    print("APROBADO")
elif ingresos>=3500000 and agnop>=5:
    print("APROBADO")
elif lugar=="R" and estadocivil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")


                          







