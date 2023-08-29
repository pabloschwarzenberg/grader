secuencia= input("ingrese secuencua de ADN:")
secuencia_mayus= secuencia.upper()
lista_secuencia=list(secuencia_mayus)
contador=[]
for base_n in lista_secuencia:
  if base_n=="A" or base_n=="T" or base_n=="G" or base_n=="C":
    contador.append(1)
  else:  
    contador.append(0)
cantidad_base_incorrecta= contador.count(0)
if cantidad_base_incorrecta>=1:
  print("secuencia incorrecta")
else:
  print("secuencia correcta")
