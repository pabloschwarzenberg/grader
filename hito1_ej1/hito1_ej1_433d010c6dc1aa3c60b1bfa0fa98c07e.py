#Nota final
PT = eval(input("Ingrese nota de Tareas: \n"))
PI = eval(input("Ingrese nota de Interrogaciones: \n"))
NE = eval(input("Ingrese nota de Examen: \n"))
PP = eval(input("Ingrese nota de Presentación: \n"))
PT1= (PT*0.3)
PI1= (PI*0.3)
NE1= (NE*0.3)
PP1= (PP*0.1)
PromedioFinal = PT1+PI1+NE1+PP1
promedioredondeado=round(PromedioFinal, 1)
print("Tú promedio final es: \n",promedioredondeado)     