#Aprobación de créditos
ig=int(input("Ingrese sus ingresos: "))
year=int(input("Año de nacimiento: "))
year= year-2022
ni=int(input("Numeros de Hijos: "))
yearb=int(input("Años de pertenencia al banco: "))
es=input("Ingrese su estado civil")
s=("soltero")
c=("casado")
vi=(input("Ingrese en donde vive"))
u=("urbano")
r=("rural")
if (yearb>10 and ni>=2):
    print("APROBADO")
elif(es==s and ni>3 and year>=45 or year<=55):
    print("APROBADO")
elif(ig>2500000 and es==s and vi==u ):
    print("APROBADO")
elif(ig>3500000 and yearb>5):
    print("APROBADO")
elif(vi==r and ni<2):
    print("APROBADO")
else:()
print("RECHAZADO")