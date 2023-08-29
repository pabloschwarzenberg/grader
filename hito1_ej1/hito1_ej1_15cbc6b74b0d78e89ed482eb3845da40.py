#Nota final
pt = float(input("nota tareas:"))
pi = float(input("nota interrogaciones:"))
ne = float(input("nota examenes:"))
pp = float(input("nota presentacion:"))

pm = (pt * 0.3) + (pi * 0.3) + (ne * 0.3) + (pp * 0.1)

print("{}".format(pm))