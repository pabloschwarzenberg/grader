#Nota final
PT = float(input('Ingrese nota final de las tareas:'))
PI = float(input('Ingrese nota final de interrogaciones:'))
NE= float(input('Ingrese nota de Examen:'))
PP =float(input('ingrese nota presentacion:'))
PF = (0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)
if(PF>4):
    print("Su promedio es:",PF,"Felicidades se ha eximido del ramo")
else:
    print("Lo sentimos el promedio es:",PF,"No se eximio del ramo")      