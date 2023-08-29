#Nota final
      #Entrada
PT = float(input("Ingrese la nota de su Tarea: "))
PI = float(input("Ingrese la nota de su Interrogaciones: "))
NE = float(input("Ingrese la nota de su Exmanen: "))
PP = float(input("Ingrese la nota de su Presentacion: "))

#Ejecucion

promedio  = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

#Salida

print("Tu promedio es: " , (format(promedio, '0.1f')))