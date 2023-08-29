#Aprobación de créditos
ingreso=eval(input("Ingreso mensual en pesos: "))
adn=eval(input("Ingrese año de nacimiento (ejemplo: 1999): "))
edad=2020-1999
ndh=eval(input("Ingrese numero de hijos: "))
adpb=eval(input("Ingrese sus años pertenencia al banco: "))
estadocivil=str(input("Ingrese su estado civil, con una C si esta casado o S soltero:"))
dv=str(input("Ingrese tipo de zona donde vive U para urbano o R para rural: "))
if(adpb>=10 and ndh>=2 or estadocivil=='C' and ndh>3 and (edad>=45 and edad<=55) or ingreso>2500000 and estadocivil=='S'  and dv=='U' or ingreso>3500000 and adpb>5 or dv=='R' and estadocivil=='C' and ndh<2):
    print("APROBADO")
else:
    print("RECHAZADO")