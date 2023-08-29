import math
def calcular_promedio_final():
    pt = float(input("nota tareas"))
    pi = float(input("nota interrogaciones"))
    ne = float(input("nota examen"))
    pp = float(input("nota presentacion"))
    s=pt*0.3
    t=pi*0.3
    a=ne*0.3
    r=pp*0.1
    final=round(s+t+r+a,1)
    return final
respuesta= calcular_promedio_final()
print(respuesta)