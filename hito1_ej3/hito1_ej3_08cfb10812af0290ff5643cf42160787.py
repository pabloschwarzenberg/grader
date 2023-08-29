#Aprobación de créditos
a=int(input("Ingreso (en pesos): "))
b=int(input("Año de nacimiento: "))
c=int(input("Numero de hijos: "))
d=int(input("Años de pertenencia al banco: "))
e=input("Estado civil (S: soltero, C: casado): ")
f=input("Vive en el campo o ciudad (U: urbano, R: rural): ")
g=2018-b
if d>10 and c>=2:
    print("APROBADO")
else:
    if c>3 and 45<g<55 and e=="C":
        print("APROBADO")
    else:
        if a>2500000 and e=="S" and f=="U":
            print("APROBADO")
        else:
            if a>3500000 and d>5:
                print("APROBADO")
            else:
                if f=="R" and c<2:
                    print("APROBADO")
                else:
                    print("RECHAZADO")