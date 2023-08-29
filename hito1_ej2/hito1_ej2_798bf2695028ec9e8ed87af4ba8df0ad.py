#Contestador de celular
numero = input("ingrese numero de telefono: ")
hora = int(input("ingrese hora: "))
 
if hora >= 0 and hora < 7:
      resultado = "CONTESTAR"
elif hora < 14:
    if numero [-3:] == "909":
        resultado = "CONTESTAR"
    else:
       resultado = "NO CONTESTAR"
elif hora >= 17 and hora < 19:
       if numero[:3] == "877":
            resultado = "NO CONTESTAR"
       else:
        resultado = "CONTESTAR"
else:
     resultado = "NO CONTESTAR"
     
print("resultado:" , resultado) 