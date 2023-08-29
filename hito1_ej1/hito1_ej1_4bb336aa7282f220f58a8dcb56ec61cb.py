#Nota final

pt = float( input("ingrese nota de tareas : " ))
pi = float( input("ingrese nota de interrogaciones : " ))
ne = float( input("ingrese nota de examen : " ))
pp = float( input("ingrese nota de presentacion : " ))

PF=  round(  (pt*0.3) +(pi*0.3)+(ne*0.3)+(pp*0.1)  ,1)

print (PF)

