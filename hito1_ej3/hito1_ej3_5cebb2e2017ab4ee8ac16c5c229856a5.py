#Aprobación de créditos

ingreso = float(input("Ingreso $"))
ano = float(input("Año de Nacimiento "))
Qhijos = float(input("Número de hijos "))
anti = float(input("Años de pertenencia al banco "))
estado = input("Estado civil S:soltero, C casado ")
campo = input("¿Donde vive? U: urbano, R: rural ")
if anti>=10 and Qhijos>=2 :
    print("APROBADO")
elif estado in ('C', 'c') and Qhijos>=3 and ((2021-ano)>=45 and (2121-ano)<=55) :
    print("APROBADO")
elif ingreso >=2500000 and estado in('S','s') and campo in('C','c') :
    print("APROBADO")
elif ingreso>=3500000 and anti>=5 :
    print("APROBADO")
elif campo in('R','r') and estado in('C','c') and Qhijos<2 :
    print("APROBADO")
else :
        print("RECHAZADO")