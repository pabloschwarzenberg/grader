#Aprobación de créditos
i=input("Ingreso:")

i=int(i)

a=input("Año de nacimiento:")

a=int(a)

n=input("Número de hijos:")

n=int(n)

ap=input("Años de pertenencia al banco:")

ap=int(ap)

e=input("Estado civil")

v=input("Donde vive:")

b=(2016-a)

if (ap>10 and n>=2):
    print("APROBADO")

elif ((e=="C" and n>3)and (a>45 and a<55)):
     print("APROBADO")

elif ((i>2500000 and e=="S") and v=="U"):
    print("APROBADO")

elif (i>3500000 and ap>5):
    print("APROBADO")

elif ((v=="R" and e=="C") and n<2):
    print("APROBADO")

else :
    print("RECHAZADO")
      