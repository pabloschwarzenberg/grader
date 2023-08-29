#Aprobación de créditos
p= eval(input("Ingrese su ingreso en pesos: "))
n= eval(input("Ingrese su año de nacimiento: "))
h= eval(input("Ingrese su cantidad de hijos: "))
ap= eval(input("Ingrese sus años de pertennecia en el banco: "))
ec= input("Ingrese su Esatdo civil ('S': soltero, 'C', casado): ")
v= input("Ingrese donde vive en campo o ciudad ('U': urbano, 'R': rural): ")
if (ap>10 and h>=2)or(ec== "C" and h>3 and 1966<=n<=1976)or (p>2500000 and ec==c and v=="U")or(p>=3500000 and ap>5)or (v=="R" and ec=="C" and h<=2):
    print(" APROBADO")
else:
    print(" RECHAZADO")
