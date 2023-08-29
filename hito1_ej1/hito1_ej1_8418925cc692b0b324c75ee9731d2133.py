#Nota final
PT=float(input("Promedio Tareas:"))
PI=float(input("Promedio Interrogaciones:"))
NE=float(input("Nota Examen:"))
PP=float(input("Promedio Presentaciones:"))
Promedio_Final = (0.3)*PT+(0.3)*PI+(0.3)*NE+(0.1)*PP
a=round(Promedio_Final,1)
if(7>=PT and 7>=PI and 7>=NE and 7>=PP):
    print("El Promedio Final es:",a)
else:
    print("Trata mejor con los promedios con decimales")