#Aprobación de créditos
ingreso=int(input("introdusca sus ingresos:"))
adn=int(input("año de nacimiento:"))
ndh=int(input("numero de hijos:"))
apb=int(input("años de pertenencia al banco:"))
ec=input("estado civil:")
coc=input("ciudad o campo:")
if apb>=10 and ndh>=2:
    print("APROBADO")
elif ec=="C" and ndh>3 and 45<=2018-adn<=55:
    print("APROBADO")
elif ingreso>=2500000 and ec=="S" and coc=="U":
    print("APROBADO")
elif ingreso>=3500000 and apb>5:
    print("APROBADO")
elif coc=="R" and ec=="C" and ndh<2:
    print("APROBADO")
else:
    print("RECHAZADO")      