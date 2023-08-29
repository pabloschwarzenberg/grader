#Nota final
pt = float(input("ingrese su nota de tareas"))
pi = float(input("ingrese su nota de interrogaciones"))
ne = float(input("ingrese su nota de examen"))
pp= float(input("ingrese su nota de presentacion"))

p = 0.3*pt+0.3*pi+0.3*ne+0.1*pp
pf = round(p,1)
print("su promedio finas es de:",pf)
