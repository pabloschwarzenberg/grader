PT = float(input("Ingresar Nota Tareas : "))
PI = float(input("Ingresar Nota Interrogacion : "))
NE = float(input("Ingresar Nota Examen : "))
PP = float(input("Ingresar Nota Presentacion :"))

PPT = 0
PPI = 0
PNE = 0
PPP = 0

cont = 1
N = 4
sumador = 0
i = 0


if PT > 0:
    PPT = 0.3*PT
    sumador = sumador + PPT       
else:
    PPT = 0
    sumador = sumador + PPT

if PI > 0:
    PPI = 0.3*PI
    sumador = sumador + PPI
else:
    PPT = 0
    sumador = sumador + PPT

if NE > 0:
    PNE = 0.3*NE
    sumador = sumador + PNE
else:
    PNE = 0
    sumador = sumador + PNE
         
if PP > 0:
    PPP = 0.1*PP
    sumador = sumador + PPP
else:
    PPP = 0
    sumador = sumador + PPP


print(round(sumador,1))