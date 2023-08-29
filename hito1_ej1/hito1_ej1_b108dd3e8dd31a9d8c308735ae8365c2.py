#Nota final
pt=float(input("ingrese nota de tareas:"))
pi=float(input("ingrese nota de interrogaciones:"))
ne=float(input("ingrese nota de examen:"))
pp=float(input("ingrese nota de presentacion:"))
x= pt*0.3
y= pi*0.3
z= ne*0.3
w= pp*0.1
print("nota final" ,round(x+y+z+w,1))