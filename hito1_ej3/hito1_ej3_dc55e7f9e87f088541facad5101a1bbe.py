ing=int(input("Ingreso: "))
an=int(input("Año de nacimiento: "))
nh=int(input("Numero de hijos: "))
ap=int(input("Años de pertenencia al banco: "))
es=input("S=Soltero, C=Casado: ")
v=input("Vivienda (U:Urbano, R:Rural): ")
edad=2020-an
if es=='s':
    es=='S'
if es=='c':
    es=='C'
if v=='u':
    v=='U'
if v=='r':
    v=='R'
if (ap>=10 and nh>=2) or (es=='C' and nh>3 and edad>=45 and edad<=55) or \
   (ing>2500000 and es=='S' and v=='U') or (ing>3500000 and ap>5) or \
   (v=='R' and es=='C' and nh<2):
    print("APROBADO")
else:
    print("RECHAZADO")
    
