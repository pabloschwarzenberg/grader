# Ingreso de numero.
numero = input("ingrese su numero de telefono: ")
hora = input("ingrese su hora de atencion: ")

# Verificacion de la hora.
try:
    hora = int(hora)
except ValueError:
    print("Error al ingresar la hora.")

# Verificacion de tamaño del numero.
if len(numero) == 8:
    print("Tamaño de numero correcto!")
    verificacion_numero = True
    
elif len(numero) < 8:
    print("Error al ingresar el numero.")
    exit()

else:  
    print("Error no esperado.")
    exit()

# Verificacion de Hora.
if hora >= 0 and hora <= 23:
    print("Hora de atencion correcta!")

# Verificacion de Emergencia.
    if hora > 0 and hora <= 7:
        print("CONTESTAR")

# Verificacion de Excepcion.   
    if hora > 0 and hora < 14:
        if (numero[5]+numero[6]+numero[7]) == "909":
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        pass       

# Verificacion de tarde.
    if hora >= 17 and hora <= 19:
        if (numero[0]+numero[1]+numero[2]) == "877":
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
    else:
        pass

# Verificacion de 19:00 hrs.
    if hora > 19:
        print("NO CONTESTAR")

else:
    print("Error al ingresar la hora")

# Verificacion de numero.
try:
    numero = int(numero)
    
except ValueError:
    print("Error al ingresar el numero.")
    exit()
