#Nota final
#pedir los numeros indicados para realizar el ejercicio
pt=float(input("Ingrese la nota de sus tareas"))
pi=float(input("Ingrese la nota de sus interrogaciones"))
ne=float(input("Ingrese la nota de su examen"))
pp=float(input("Ingrese la nota de su presentacion"))
#calculo de el ejercico
Nota_final= (pt*0.3) + (pi*0.3)+(ne*0.3)+(pp*0.1)
#Resultado
print("Su nota final es:",round(Nota_final,1))
