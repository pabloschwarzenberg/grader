# ENTRADA DEL EJERCICIO
PT = float(input("Enter note from Taeas: "))
PI = float(input("Enter note of Interrogations:"))
NE = float(input("Enter Exam grade:"))
PP = float(input("Enter note Presentations : "))
# PROCESAMIENTO 2.0 
nota_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP
# SALIDA LUCHO
print("The final grade for the course is: ", round(nota_final,1))