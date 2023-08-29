#Nota final

pt_tarea = float(input("¿Cual fue la nota de la tarea?:)"))
pi_interrogaciones = float(input("¿Cual fue la nota de la interrogacion?:)"))
ne_examen = float(input("¿Cual fue la nota del examen?:)"))
pp_presentacion = float(input("¿Cual fue la nota de la presentacion?:)"))

promedio = 0.3*pt_tarea + 0.3*pi_interrogaciones  + 0.3*ne_examen + 0.1*pp_presentacion 

print("La nota toal fue:", round(promedio,1))    