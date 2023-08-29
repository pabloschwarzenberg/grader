#Nota final
notaPT=0
while (notaPT<1 or notaPT>7):
  notaPT=float(input("Tu nota de tareas: "))

notaPI=0
while (notaPI<1 or notaPI>7):
  notaPI=float(input("Tu nota de interrogaciones: "))

notaNE=0
while (notaNE<1 or notaNE>7):
  notaNE=float(input("Tu nota de examen: "))

notaPP=0
while (notaPP<1 or notaPP>7):
  notaPP=float(input("Tu nota de presentacion: "))

notaFinal=(0.3*notaPT)+(0.3*notaPI)+(0.3*notaNE)+(0.1*notaPP)
notaFinalRedondeada= round(notaFinal, 1)
print("Tu nota final es un",notaFinalRedondeada,)