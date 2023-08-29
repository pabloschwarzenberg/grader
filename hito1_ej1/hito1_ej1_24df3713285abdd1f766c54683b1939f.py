#Nota final
def promedio(w,x,y,z):
    w = round(w,1)
    w = w*0.3
    x = round(x,1)
    x = x*0.3
    y = round(y,1)
    y = y*0.3
    z = round(z,1)
    z = z*0.1
    prom = w+x+y+z
    prom = round(prom,1)
    return prom
print("Ingresar Notas")
PT = input("Ingrese nota de Tareas") # Tarea
PT = round(float(PT),1)
PI = input("Ingrese nota de Interrogacion")#Interrogacion
PI = round(float(PI),1)
NE = input("Ingrese nota de Examen")#Examen
NE = round(float(NE),1)
PP = input("Ingrese nota de Presentacion")#Presentacion
PP = round(float(PP),1)

Pr = promedio(PT,PI,NE,PP)
print(Pr)