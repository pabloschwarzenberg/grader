#Nota final

tare = float(input("¿Cuál es su nota en las tareas?: "))
interr = float(input("¿Cuál es su nota en las interrogaciones ?: "))
exam = float(input("¿Cuál fue su nota en el examen final?: "))
presen = float(input("¿Cuál fue su nota en la presentacion?: "))

pt = ((tare * 30)/100)
p_i =((interr * 30)/100)
ne = ((exam * 30)/100)
pp = ((presen * 10)/100)


resultado = pt + p_i+ ne+pp

resultado = round(resultado,1)

print(resultado)