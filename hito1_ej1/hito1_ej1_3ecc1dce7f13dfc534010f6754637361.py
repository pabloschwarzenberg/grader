PT=eval(input("Ingreso nota Tareas:"))
PI=eval(input("Ingrese nota Interrogaciones:"))
NE=eval(input("Ingrese nota Examen:"))
PP=eval(input("Ingrese nota Presentacion:"))
promedio=PT*0.3+PI*0.3+NE*0.3+PP*0.1
print("Final es:", round(promedio,1))