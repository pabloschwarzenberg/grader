#Nota final
      
pt = float(input("Ingrese nota Tareas:"))
pi = float(input("Ingrese nota Interrogaciones:"))
ne = float(input("Ingrese nota Examen:"))
pp = float(input("Ingrese nota Presentacion:"))

pt1 = (pt*0.3)
pi1 = (pi*0.3)
ne1 = (ne*0.3)
pp1 = (pp*0.1)

result = (pt1+pi1+ne1+pp1)

print(round(result, 1))