# Obtener la hora del día y el número de teléfono del usuario
hora = int(input("Ingrese la hora del día (formato 24 horas): "))
numero_telefono = input("Ingrese el número de teléfono (8 dígitos): ")

# Verificar las reglas para determinar si se debe contestar o no la llamada
contestar = False

if 0 <= hora < 7:
    contestar = True
elif hora < 14 and numero_telefono.endswith("909"):
    contestar = True
elif 17 <= hora < 19 and not numero_telefono.startswith("877"):
    contestar = True

# Imprimir si se debe contestar o no la llamada
if contestar:
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
