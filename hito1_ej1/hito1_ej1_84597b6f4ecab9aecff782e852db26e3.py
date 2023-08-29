#Nota final
PT=float(input("Nota de tareas:"))
PI=float(input("Nota de interrogaciones:"))
NE=float(input("Nota de examen:"))
PP=float(input("Nota de presentacion:"))
vrt=PT*0.3
vri=PI*0.3
vre=NE*0.3
vrp=PP*0.1
total=vrt+vre+vri+vrp
print(total)