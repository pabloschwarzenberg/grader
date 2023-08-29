#Descomponer un número
digitos = []
numero = input("")
for digito in numero:
  digitos.append(digito)
if len(digitos) == 4:    
    if digitos[0] != "0":
      print(digitos[0]+"M", end=" + ")
    if digitos[1] != "0":
      print(digitos[1]+"C", end=" + ")
    if digitos[2] != "0":
      print(digitos[2]+"D", end=" + ")
    print(digitos[3]+"U")
if len(digitos) == 3:    
    if digitos[0] != "0":
      print(digitos[0]+"C", end=" + ")
    if digitos[1] != "0":
      print(digitos[1]+"D", end=" + ")
    print(digitos[2]+"U")
if len(digitos) == 2:    
    if digitos[0] != "0":
      print(digitos[0]+"D", end=" + ")
    print(digitos[1]+"U")
if len(digitos) == 1:    
    print(digitos[0]+"U")

      