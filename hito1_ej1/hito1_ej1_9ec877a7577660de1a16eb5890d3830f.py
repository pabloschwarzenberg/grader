#Nota final
pt = float(input("ingresa P_tareas: "))
pi = float(input("ingresa p_interrogaciones: "))
ne = float(input("ingresa n_examen: "))
pp = float(input("ingresa p_presentacion: "))

p_final = (0.3*pt) + (0.3*pi)+ (0.3*ne)+(0.1*pp)
p_final = print(round(p_final,1))
print("el p_f de las notas es" ,p_final)
            