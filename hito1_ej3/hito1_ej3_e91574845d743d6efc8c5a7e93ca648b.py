print("Porfavor reponda las sigiuntes preguntas")
a1=float(input("Ingreso en pesos:"))
b1=int(input("Año de nacimiento:"))
c1=int(input("Número de hijos:"))
d1=int(input("Años de pertenencia al banco:"))
e1=str(input("Estado civil (S: soltero, C, casado):"))
f1=str(input("Vive en campo o cuidad (U: urbano, R: rural):"))
if(d1>10) and(c1>=2):
    print("APROBADO")
elif("C"==e1) and(c1>3)and(b1>1961) and(b1<1971):
    print("APROBADO")
elif(a1>2500000) and("S"==e1) and(f1=="U"):
    print("APROBADO")
elif(a1>3500000) and(d1>5):
    print("APROBADO")
elif(f1=="R") and("C"==e1)and(c1<2):
    print("APROBADO")
else:
    print("RECHAZADO")

