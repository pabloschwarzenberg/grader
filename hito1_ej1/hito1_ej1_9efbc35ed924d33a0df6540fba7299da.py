#Nota final
#CALCULO DE PROMEDIO

PT = float(input("ingrese nota de Tareas"))
PI = float(input("ingrese nota de Interrogaciones"))    
NE = float(input("ingrese nota de Examen"))         
PP = float(input("ingrese nota de Presentacion"))


promedio = PT*0.3 + PI*0.3 + NE*.3 + PP*0.1


print("Su promedio final es :","{:.1f}".format(promedio))