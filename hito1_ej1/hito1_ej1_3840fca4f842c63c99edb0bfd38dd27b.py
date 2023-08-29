#Nota final
print("<<<<<NOTA FINAL>>>>>")
PT = float(input("INGRESE NOTA DE TAREAS: ")) 
PI = float(input("INGRESE NOTA DE INTERROGACIONES "))
PE = float(input("INGRESE NOTA DE EXAMEN: "))
PP = float(input("INGRESE NOTA DE PRESENTACIÓN "))
NF = (0.3*PT)+(0.3*PI)+(0.3*PE)+(0.1*PP)
print(round(NF,1))
