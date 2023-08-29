palabra=input("ingrese palabra")
palabra=palabra.lower()
estado= True
for x in palabra:
    if x=="a" or x== "c" or x=="t" or x=="g":
      pass
    else:
      estado= False
      break
if estado==False:
   print("secuencia incorrecta")
else:
  print("secuencia correcta")
  