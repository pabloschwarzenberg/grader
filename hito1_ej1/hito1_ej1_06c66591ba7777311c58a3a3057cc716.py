#Nota final
PT = float(input('ingrese nota de tarea:'))

PI = float(input('ingrese nota de interrogacion:'))

NE = float(input('ingrese nota de examen:'))

PP = float(input('ingrese nota de presentacion:'))
                 
TT = (0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP)
               
print(round(TT, 1))