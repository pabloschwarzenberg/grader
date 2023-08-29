#Nota final
PT=float(input("ingresa nota de tarea:" ))
PI=float(input("ingresa nota de interrogacion:" ))
NE=float(input("ingresa nota del examen:" ))
PP=float(input("ingresa nota de presentacion:" ))

Prom=float(float(0.3)*(PT+PI+NE)+float(0.1)*PP)
print(round(Prom,1))