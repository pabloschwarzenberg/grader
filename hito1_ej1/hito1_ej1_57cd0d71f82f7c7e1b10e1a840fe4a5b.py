#INGRESO DE NOTAS 
print("ingrese sus notas de: ")
PT=float(input("PT (Tareas)= "))
PI=float(input("PI (Interrogaciones)= "))
NE=float(input("NE (Examen)= "))
PP=float(input("PP (Presentacion)= "))
#FORMULA 
X=(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
round(X, 3)
#RESULTADO 
print("su promedio de notas es",X)