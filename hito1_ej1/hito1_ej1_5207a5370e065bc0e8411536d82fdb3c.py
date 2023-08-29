#Nota final
NotaPT=0
while (NotaPT<1 or NotaPT>7):
  NotaPT=float(input("Nota de tareas: "))
NotaPI=0
while (NotaPI<1 or NotaPI>7):
  NotaPI=float(input("Nota de interrogaciones: "))
NotaNE=0
while (NotaNE<1 or NotaNE>7):
  NotaNE=float(input("Nota de examen: "))
NotaPP=0
while (NotaPP<1 or NotaPP>7):
  NotaPP=float(input("Nota de presentacion: "))
PromedioFinal=(NotaPT*0.30)+(NotaPI*0.30)+(NotaNE*0.30)+(NotaPP*0.10)
print("Tu promedio final es un",round(PromedioFinal,1))