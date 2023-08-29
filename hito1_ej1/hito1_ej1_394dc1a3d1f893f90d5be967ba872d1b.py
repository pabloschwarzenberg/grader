PT = float(input("ingrese promedio tareas: "))
PI = float(input("ingrese promedio interrogaciones: "))
NE = float(input("ingrese nota examen: "))
PP = float(input("ingrese nota de presentacion: "))
PF = (PT*0.3)+(PI*0.3)+(NE*0.3)+(PP*0.1)
N = str(PF)
E = ((PF*1000)%1000)
E = E%100
if E >=50:
    PF = PF + 0.1
PF = (PF*10)//1
PF = PF/10
N = str(PF)
print ("su promedio final es:" +(N))