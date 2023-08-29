#Nota final
pt=float(input("ingrese nota tareas:"))
pi=float(input("ingrese nota interrogaciones:"))
ne=float(input("ingrese notas examne: "))
pp=float(input("ingrese notas presentacion"))
suma= 0.3*pt+0.3*pi+0.3*ne+0.1*pp
suma_redondeo=round(suma, 1) 
print({suma_redondeo})