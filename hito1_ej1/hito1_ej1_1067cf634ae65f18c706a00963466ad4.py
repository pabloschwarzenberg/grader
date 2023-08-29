#Nota final
PT = float(input("Nota Tareas: "))
PI = float(input("Nota Interrogaciones: "))
NE = float(input("Nota Examen: "))
PP = float(input("Nota Presentacion: "))

PTX = round(0.3*PT,1)
PIX = round(0.3*PI,1)
NEX = round(0.3*NE,1)
PPX = round(0.1*PP,1)

print(PTX+PIX+NEX+PPX)

  

