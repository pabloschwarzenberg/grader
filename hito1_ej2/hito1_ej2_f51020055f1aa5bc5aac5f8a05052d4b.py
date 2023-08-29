#Contestador de celular
Telefono = int(input("Ingrese numero telefonico: "))   
Horario = int(input("Ingrese hora de la llamada: "))
strTelefono = str(Telefono)
ultimo_digito = strTelefono[5:8]
primer_digito = strTelefono[1:4]
Resultado = ""

print(strTelefono)
print(ultimo_digito)
print(primer_digito)

if Horario>=0 and Horario<=7:
   Resultado = "CONTESTAR"
else:
  if Horario<=14 and ultimo_digito=="909":
    Resultado = "CONTESTAR"
  else:
     if Horario>=17 and Horario<=19 and primer_digito=="877":
        Resultado = "CONTESTAR"
     else: 
        Resultado = "NO CONTESTAR"
        
        
print("Resultado: "+Resultado)
