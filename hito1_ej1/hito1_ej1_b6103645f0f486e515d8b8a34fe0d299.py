#Nota final
pt = float(input("ingrece nota de tareas:"))
pi = float(input("ingrece nota de interrogaciones:"))
ne = float(input("ingrece nota de examenes:"))
pp = float(input("ingrece nota de presentacones:"))
x = ((0.3*pt + 0.3*pi + 0.3 *ne + 0.1*pp))
c = round(x,1)
print("su promedio final es:", c)      