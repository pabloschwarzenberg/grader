#Nota final
print("hola, vamos a calcular tus notas")
PT=0
while(PT<1 or PT>8):
    PT=float(input("ingrese su primera nota de tarea: "))
PI=0
while(PI<1 or PI>8):
    PI=float(input("ingrese su segunda nota de interrogaciones: "))
NE=0
while(NE<1 or NE>8):
    NE=float(input("ingrese su tercera nota de Examen: "))
PP=0
while(PP<1 or PP>8):
    PP=float(input("ingrese su cuarta nota de presentacion: "))
total=round((0.3*PT) + (0.3*PI) + (0.3*NE)+ (0.1*PP), 1)
print("tus notas totales son ",total)
