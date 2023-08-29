#Nota final
PT= float(input("ingrese nota tarea:" ))
PI= float(input("ingrese nota interrogacion:" ))
NE= float(input("ingrese nota examen:" ))
PP= float(input("ingrese nota presentacion:" ))			
Pfinal=(0.3*(PT+PI+NE)+(0.1*PP))
Pfinal=round((Pfinal),1)
print(str(Pfinal))       