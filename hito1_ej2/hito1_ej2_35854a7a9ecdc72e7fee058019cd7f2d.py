# Obtener el número telefónico y la hora de la llamada
numero_telefonico = input("Ingrese número telefónico: ")
hora_llamada = int(input("Ingrese hora de la llamada: "))

# Verificar si se debe contestar o no
if hora_llamada >= 0 and hora_llamada <= 7:
    print("Resultado: CONTESTAR")
elif hora_llamada < 14:
    if numero_telefonico.endswith("909"):
        print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")
elif hora_llamada >= 17 and hora_llamada <= 19:
    if numero_telefonico.startswith("877"):
        print("Resultado: NO CONTESTAR")
    else:
        print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")