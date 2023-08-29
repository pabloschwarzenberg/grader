#Nota final
def notacalculada(PT, PI, NE, PP):
  return(PT*0.3) + (PI*0.3) + (NE*0.3) + (PP*0.1)


PT = float(input("ingrese la nota de trabajos: "))
PI = float(input("ingrese la nota de interrogaciones: "))
NE = float(input("ingrese la nota del examen: "))
PP = float(input("ingrese la nota de presentacion: "))


nota_promediada = notacalculada(PT, PI, NE, PP)

print("la nota promediada final es: ",nota_promediada)