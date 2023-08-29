#Aprobación de créditos
ingreso=int(input("Ingreso (en pesos): "))
nacimiento=int(input("Año de nacimiento: "))
hijos=int(input("Numero de hijos: "))
banco=int(input("Años en el banco: "))
ecivil=input("Estado civil: ")
lugar=input("Campo o ciudad: ")
edad=2016-nacimiento

if banco>10 and hijos>=2:
    print("APROBADO")
elif ecivil=="C" and hijos>3 and edad>=45 and edad<=55:
    print("APROBADO")
elif ingreso>2500000 and ecivil=="S" and lugar=="U":
    print("APROBADO")
elif ingreso>3500000 and banco>5:
    print("APROBADO")
elif lugar=="R" and ecivil=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")