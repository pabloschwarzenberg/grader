#Nota final
pt_ = float(input("Favor ingrese la nota de Tareas: "))
pi_ = float(input("Favor ingrese la nota de Interrogaciones: "))
ne_ = float(input("Favor ingrese la nota de Examen: "))
pp_ = float(input("Favor ingrese la nota de Presentacion: "))

promedio = ( pt_ * 0.3 ) + ( pi_ * 0.3 ) + ( ne_ * 0.3 ) + ( pp_ * 0.1 ) 

print("Promedio: ", round(promedio, 1))      
