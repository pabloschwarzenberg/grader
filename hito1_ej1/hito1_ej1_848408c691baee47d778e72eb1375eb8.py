#Nota final
#-------------------------------------------------------#
#-------------------------------------------------------#
class Notas:
 while True:
     try:
         PT = float(input("Ingresa tu nota de Tareas"))
         PI = float(input("Ingresa tu nota de Interrogaciones"))
         NE = float(input("Ingresa tu nota de Examen"))
         PP = float(input("Ingresa tu nota de Presentacion"))         
         if PT < 0 or PI < 0 or NE < 0 or PP < 0 or PT > 7 or PI > 7 or NE > 7 or PP > 7:
            print("¡ERROR! Tu nota debe estar en el rango de 1-7")
            continue
         break
     except:
        print("¡ERROR! Tu nota es invalida, ingresela nuevamente")
#-------------------------------------------------------#
def Calculo():
    NotaFinal = round(Notas.PT*0.3 + Notas.PI*0.3 + Notas.NE*0.3 + Notas.PP*0.1, 1)
    print("El promedio final de las notas ingresadas es: {}" .format(NotaFinal))
#-------------------------------------------------------# 
Calculo()
#-------------------------------------------------------#       