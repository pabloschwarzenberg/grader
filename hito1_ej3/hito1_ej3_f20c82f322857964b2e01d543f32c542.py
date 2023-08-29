#Aprobación de créditos
ingreso=int(input("ingrese el ingreso suyo en pesos"))
edad=int(input("ingrese edad"))
numerodehijos=int(input("ingrese numero de hijos"))
añosdepertenenciaalbanco=int(input("ingrese años de pertenencia al banco"))
estadocivil=input("ingrese estado civil (S) para soltero y (C) para casados")
viveen=input("ingrese donde vive (U) urbano o (R) rural")
if  añosdepertenenciaalbanco>10 and numerodehijos>2:
    print("APROBADO")
elif    estadocivil=="C" and numerodehijos>3 and 45<edad<=55:
    print("APROBADO")
elif    ingreso>2500000 and estadocivil=="S" and viveen=="U":
    print("APROBADO")
elif    ingreso>3500000 and añosdepertenenciaalbanco>5:
    print("APROBADO")
elif    viveen=="R" and estadocivil=="C" and numerodehijos<2:
    print("APROBADO")