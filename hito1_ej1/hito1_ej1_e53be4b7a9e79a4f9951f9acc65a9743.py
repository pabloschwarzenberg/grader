#Nota final
PT = float(input('Ingrese nota porcentaje Tareas "PT": '))
PI = float(input('Ingrese nota porcentaje Interrogaciones "PI": '))
NE = float(input('Ingrese nota Examen "NE": '))
PP = float(input('Ingrese nota porcentaje Presentacion "PP": '))

PF = (PT*30)/100 + (PI*30)/100 + (NE*30)/100  + (PP*10)/100
print('           El Porcentaje Final es:')

print(round(PF,1))
  