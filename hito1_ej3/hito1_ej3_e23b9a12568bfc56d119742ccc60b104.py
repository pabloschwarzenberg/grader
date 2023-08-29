#Aprobación de créditos
ingreso= int(input("Ingrese su Ingreso en $ : "))
año= int(input("Ingrese su año de nacimiento: "))
nhijos= int(input("Ingrese su cantidad de hijos: "))
añosb= int(input("Ingrese la cantidad de años con nuestro banco: "))
ecivil= str(input("Ingrese su estado civil (S) O (C) "))
viv= str(input("Ingrese el lugar donde vive (U) O (R) "))
edad=2021-año

if ((añosb>10) and (nhijos>=2)):
    print("APROBADO")
elif ((ecivil== "C" or ecivil== "c") and (edad>=45 and edad<=55) and (nhijos>3)):
    print("APROBADO")
elif ((ingreso>2500000) and (ecivil=="S" or ecivil=="s") and (viv=="U" or viv=="u")):
    print("APROBADO")
elif ((ingreso>3500000) and (añosb>5)):
    print("APROBADO")
elif ((viv=="R" or viv=="r") and (ecivil=="C" or ecivil=="c") and (nhijos<2)):
    print("APROBADO")
else:
    print("REPROBADO")      