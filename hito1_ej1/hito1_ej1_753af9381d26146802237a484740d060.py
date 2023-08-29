#Nota final
PT = 0
PI = 0
NE = 0
PP = 0
PF = 0
#Saludar y solicitar notas
print("Hola, para calcular tu promedio final debes ingresar los datos que acontinuación te serán solicitados")
PT = eval(input("La nota de tareas es: "))
PI = eval(input("La nota de interrogaciones es: "))
NE = eval(input("La nota del examen es: "))
PP = eval(input("La nota de la presentación es: "))
PF = (0.3*PT) + (0.3*PI) + (0.3*NE) + (0.1*PP)
print("Tu promedio final es: ", PF)