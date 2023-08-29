#Contestador de celular
      # Solicitamos al usuario la hora y el número de teléfono

telefono = int(input("Ingrese numero telefonico: "))

hora = int(input("Ingrese hora de la llamada: "))

 

# Comprobamos las diferentes condiciones y decidimos si contestar o no

if 0 <= hora < 7:

    print("CONTESTAR")

elif 7 <= hora < 14:

    if str(telefono).endswith("909"):

        print("CONTESTAR")

    else:

        print("NO CONTESTAR")

elif 14 <= hora < 17:

    print("NO CONTESTAR")

elif 17 <= hora < 19:

    if str(telefono).startswith("877"):

        print("NO CONTESTAR")

    else:

        print("CONTESTAR")
else:

    print("NO CONTESTAR")