#Nota final
      #recopilacion de datos(usuario)
PT = float(input("Ingrese la nota PT: "))
PI = float(input("Ingrese la nota PI: "))
NE = float(input("Ingrese la nota NE: "))
PP = float(input("Ingrese la nota PP: "))

#Cálculo
promedio_final = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

#salida
print("El promedio final es:", round(promedio_final, 1))