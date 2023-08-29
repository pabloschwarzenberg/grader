#Nota final
PT = float(input("Ingrese su calificación PT: "))
PI = float(input("Ingrese su calificación PI: "))   
NE = float(input("Ingrese su calificación NE: "))   
PP = float(input("Ingrese su calificación PP: "))  

prom_final = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP

round_prom = round(prom_final, 1)

print(round_prom)