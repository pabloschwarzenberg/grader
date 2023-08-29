print("Ingrese sus notas en este orden PT, PI, Ne, PP \nPT= Tareas \nPI= Interrogaciones \nNE= Examen \nPP= Presentacion")
a,b,c,d = input("Ingrese aqui sus notas: ").split()

promedio = float(a)*0.3 + float(b)*0.3 + float(c)*0.3 + float(d)*0.1
print(round(promedio, 3))
