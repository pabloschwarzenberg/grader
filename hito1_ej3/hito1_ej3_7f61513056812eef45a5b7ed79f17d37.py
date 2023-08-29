#Aprobación de créditos
a=int(input("Ingreso en pesos: "))
b=int(input("Año de nacimiento: "))
c=int(input("Numero de hijos: "))
d=int(input("Años de pertenencia al banco: "))
e=input("Estado civil: ")
f=input("Localidad Urbana[U] o Rural[R]: ")
x=str("C")
y=str("S")
w=str("R")
z=str("U")
if d>10 and c>=2 :
    print("APROBADO")
elif e==x and c>3 and 1962<=b<=1972 :
    print("APROBADO")
elif a>2500000 and e==y and f==z :
    print("APROBADO")
elif a>3500000 and d>5 :
    print("APROBADO")
elif f==w and e==x and c<2 :
    print("APROBADO")
else :
    print("REPROBADO")