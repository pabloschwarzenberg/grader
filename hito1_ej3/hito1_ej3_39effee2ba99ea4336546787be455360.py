#Aprobación de créditos
ingreso=int(input("Ingrese su renta:\n"))
anacimiento=int(input("año de nacimiento:\n"))
numhijos=int(input("cuántos hijos:\n"))
tbanco=int(input("años en el banco:\n"))
ecivil=input("estado civil S o C:\n")
habita=input("Urbano o Rural U o R:\n")
edad=2022-anacimiento

if (tbanco>=10 and numhijos>=2) or (ecivil=="C" and numhijos>3 and edad>=45 and edad<=55) or (ingreso>2500000 and ecivil=="S" and habita=="U") or (ingreso>3500000 and tbanco>5) or (habita=="R" and ecivil=="C" and numhijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")