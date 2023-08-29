#Nota final
PT=input("Ingrese nota Tareas:")
PI=input("Ingrese nota Interrogaciones:")
NE=input("Ingrese nota Examen:")
PP=input("Ingrese nota Presentacion:")

Calculo = (0.3*float(PT)) + (0.3*float(PI)) + (0.3*float(NE)) + (0.1*float(PP))
print( "{:.{}f}".format( Calculo,1 ) )