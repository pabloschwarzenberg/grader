#Nota final
pT = float(input("Nota Tareas: "))
pI = float(input("Nota Interrogaciones: "))
nE = float(input("Nota Examen: "))
pP = float(input("Nota Presentación: "))
pT = pT*0.3
pI = pI*0.3
nE = nE*0.3
pP = pP*0.1
notaF= pT+pI+nE+pP
notaF = round(notaF, 1)
print(notaF)
      