#Nota final
PT = float(input("Nota Tareas: "))

PI = float(input("Nota Interrogaciónes: "))

NE = float(input("Nota Examen: "))

PP = float(input("Nota Presentación : "))


final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP   
print("La Nota Final es: ", round(final,1))