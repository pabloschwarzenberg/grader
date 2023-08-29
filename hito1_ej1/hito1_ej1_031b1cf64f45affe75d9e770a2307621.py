#Nota final
PT = float(input (" Tareas: "))
if PT>=0:
    A = [PT]
    (print (A))
PI = float(input (" Interrogaciones: "))
if PI>=0:
    B = [PI]
    (print (B))
NE = float(input (" Examen: ")) 
if NE>=0:
    C = [NE]
    (print (C))
PP = float(input (" Presentacion: ")) 
if PP>=0:
    D = [PP]
    (print (D))
y= float(0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP)
if y>=0:
    print(y)

