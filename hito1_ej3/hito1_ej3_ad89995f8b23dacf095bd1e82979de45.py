##Aprobacion de creditos
print("Hola, a continuacion ingrese datos requeridos para aprobar su credito")
i=int(input("Indique su Ingreso:"))
a=int(input("Ingrese año de nacimiento:"))
n=int(input("Indique numero de hijos:"))
an=int(input("Indique años de pertenecia al banco:"))
e=(input("Estado civil (¨S¨:soltero,¨C¨:casado:"))
c=(input("Indique vivienda (¨U¨:urbano, ¨R¨:rural:"))
#datos
C=0
S=0
U=0
R=0
if an >10 and n>=2:
    print("Felicidades,a sido APROBADO su credito")
if e==C and n>3 and 1959 < a <1967:
    print("Felicidades,a sido APROBADO su credito")
if i>2500000 and e==S and c==U:
    print("Felicidades,a sido APROBADO su credito")
if i>3500000 and an>5:
    print("Felicidades,a sido APROBADO su credito")
if c==R and e==C and n<2:
    print("Felicidades,a sido APROBADO su credito")
if i<50000 and a<1959 and n>=2 and an<5 and e==S and c==R :
    print("Lo sentimos ustes a sido RECHAZADO en su credito")
else:
    print("Felicidades,a sido APROBADO su credito")

      