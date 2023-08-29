#Nota final
def calcular_promedio():
    PT = float(input("ingrese la nota de Tareas:"));
    PI = float(input("ingrese la nota de Interrogaciones:"));
    NE = float(input("ingrese la nota de Examen:"));
    PP = float(input("ingrese la nota de Presentacion:"));
    nota = 0.3*PT + 0.3*PI + 0.3*NE + 0.1*PP;
    promedio = round(nota,1);
    return(promedio) 
print(calcular_promedio())