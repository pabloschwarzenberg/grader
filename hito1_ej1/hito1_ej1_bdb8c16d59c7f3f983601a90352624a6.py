#Nota final
Val_PT = float
Val_PI = float
Val_NE= float
Val_PP= float
Val_Promedio= float



Val_PT = float(input("Ingrese Nota tarea : "))
Val_PI = float(input("Ingrese Nota Interrogación : "))
Val_NE = float(input("Ingrese Nota NE : "))
Val_PP = float(input("Ingrese Nota Presentación: "))




Val_PT = round((Val_PT * 0.3),1)
Val_PI = round((Val_PI * 0.3),1)
Val_NE = round((Val_NE * 0.3),1)
Val_PP = round((Val_PP * 0.1),1)



Val_Promedio= round((Val_PT+Val_PI+Val_NE+Val_PP), 1)
print("Promedio es : ", format(Val_Promedio))