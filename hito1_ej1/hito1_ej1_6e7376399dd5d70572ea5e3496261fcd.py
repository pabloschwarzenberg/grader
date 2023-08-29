#Nota final
pt=eval(input("ingrese su puntaje de las tareas: "))
pi=eval(input("ingrese su puntaje en las interrogaciones: "))
ne=eval(input("ingrese su nota en examen"))
pp=eval(input("ingrese su puntaje en la presentacion: "))
promedio=(pt*0.3)+(pi*0.3)+(ne*0.3)+(pp*0.1)
print("la nota final es: ",round(promedio,1))     