#Contestador de celular
#Entradas
num_te = str(int(input("El número que llama es: ")))
h_llam = int(input("La hora de la llamada es: "))
num_ini = num_te[0:3]
num_fin = num_te[5:8]
#Ecuación
if h_llam >= 0 and h_llam <= 7:
  print("Contestar")
elif h_llam >= 8 and h_llam <= 14:
  if num_fin == "909":
    print("Contestar")
  else:
    print("No Contestar")
elif h_llam >= 15 and h_llam <= 17:
   if num_in == "877":
     print("No Contestar")
   else:
    print("Contestar")
else: 
  print("no contestar")