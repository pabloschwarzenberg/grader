#Nota final
PT=float(input("tareas"))
PI=float(input("interrgaciones"))
NE=float(input("examenes"))
PP=float(input("presentacion"))
v=(PT+PI+NE)*0.3
PP=PP*0.1
r=round((v+PP),1)
print(str(r))
