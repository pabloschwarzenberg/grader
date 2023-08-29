#Nota final
def calcular_promedio_final(PT, PI, NE, PP):
    promedio = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP  #Calcular promedio final
    
    return round(promedio, 1) #Redondear el promedio a un decimal
    
#El usurario ingresa las notas
PT = float(input("ingresar notas tareas (PT):"))
PI = float(input("ingresar notas interrogaciones (PI):"))
NE = float(input("ingresar notas examen(NE):"))
PP = float(input("ingresar nota presentación:"))

#Calcular promedio final 
promedio_final = calcular_promedio_final(PT, PI, NE, PP)

#Imprimir resultado
print("El promedio final es:", promedio_final)