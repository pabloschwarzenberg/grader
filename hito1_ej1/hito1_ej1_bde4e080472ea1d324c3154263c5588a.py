#Nota final

def promedio_final():
    pt = float(input("Nota Tareas (PT): "))
    pi = float(input("Nota Interrogaciones (PI): "))
    ne = float(input("Nota Examen (NE): "))
    pp = float(input("Nota Presentación (PP): "))
    
    promedio = 0.3*(pt) + 0.3*(pi) + 0.3*(ne) + 0.1*(pp)
    
    promedio_redondeado = round(promedio, 1)
    
    print("El promedio final es", promedio_redondeado)

promedio_final()