#Contestador de celular

# Solicitar el número telefónico y la hora de la llamada al usuario

numero_telefonico = input("Ingrese número telefónico: ")

hora_llamada = int(input("Ingrese hora de la llamada: "))

 

# Verificar las condiciones para determinar si se contesta o no la llamada

if hora_llamada >= 0 and hora_llamada <= 7:

    # Si la llamada ocurre entre 00:00 y 07:00, se contesta

    print("CONTESTAR")

elif hora_llamada < 14 and not numero_telefonico.endswith("909"):

    # Si ocurre antes de las 14:00 y el número no termina en 909, se contesta

    print("CONTESTAR")

elif hora_llamada >= 17 and hora_llamada <= 19 and not numero_telefonico.startswith("877"):

    # Durante la tarde, se contesta entre 17:00 y 19:00 si el número no comienza por 877

    print("CONTESTAR")
 else
 
 # En cualquier otro caso, no se contesta

    print("NO CONTESTAR")