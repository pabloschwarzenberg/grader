# Pedir al usuario el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese hora de la llamada (entre 0 y 23): "))

# Verificar si contestar o no
if hora_llamada < 7:
    print("CONTESTAR")
elif hora_llamada < 14 and numero_telefonico % 100 == 909:
    print("CONTESTAR")
elif 17 <= hora_llamada < 19 and numero_telefonico // 100000 == 877:
    print("NO CONTESTAR")
else:
    print("NO CONTESTAR")
