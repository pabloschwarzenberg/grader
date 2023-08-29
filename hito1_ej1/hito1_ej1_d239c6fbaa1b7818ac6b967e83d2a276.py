tarea=float(input("dame la nota de tareas")) 
interrogaciones=float(input("dame la nota de interrogaciones"))     
examen=float(input("dame la nota de examen")) 
presentacion=float(input("dame la nota de presentacion"))
x=(tarea*0.3)+(examen*0.3)+(presentacion*0.1)+(interrogaciones*0.3)
x=str(x)
if int(x[2])<5:
    x=x[0]+x[1]+x[2]
else:
    if int(x[2])<9:
        y=int(x[2])+1
        y=str(y)
        x=x[0]+x[1]+y
    else:
        x=float(x[0])+1
        x=float(x)
print(x)