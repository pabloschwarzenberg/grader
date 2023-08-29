#Aprobación de créditos
i=int(input("Ingreso en pesos: $"))
N=int(input("Año de nacimiento: "))
h=int(input("Número de hijos: "))
a=int(input("Años de pertenecia al banco: "))
e=input("Estado civil, S para soltero o C para casado: ")
v=input("Lugar de residencia, U urbano o R rural: ")
n=2017-N

if a>10 and h>=2:
    print("APROBADO")
elif e=='C' and h>3 and 45<n<55:
    print("APROBADO")
elif i>2500000 and e=='S' and v=='U':
    print("APROBADO")
elif i>3500000 and a>5:
    print("APROBADO")
elif v=='R' and e=='C' and h<2:
    print("APROBADO")

else:
    print("RECHAZADO")