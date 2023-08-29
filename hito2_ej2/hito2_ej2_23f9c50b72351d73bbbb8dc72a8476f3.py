palabra=str(input("Ingrese una palabra"))
no_secuencia="bdefhijklmnopqrsuvwxyz"
for i in no_secuencia:
  secuencia=palabra.find(i)
  if secuencia==[-1]:
    print("secuencia correcta")
  elif secuencia!=[-1]:
    print("secuencia incorrecta")