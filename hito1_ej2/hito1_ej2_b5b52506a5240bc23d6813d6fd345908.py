#Contestador de celular
# Entradas
numero_telefono = int(input("Ingrese el numero de telefono: "))
hora_llamada = int(input("Ingrese la hora de llamada: "))
last = (numero_telefono//1)%1000
one = (numero_telefono//100000)

# Procesamiento
if 0 < hora_llamada < 23:
    if 0 < hora_llamada < 7:
        print("Contestar")
    elif 14 > hora_llamada > 7 and last == 909:
        print("Contestar")
    elif 14 > hora_llamada > 7:
        print("No contestar")
    elif 19 > hora_llamada > 17 and one == 877:
        print("No Contestar")
    elif 19 > hora_llamada > 17:
        print("Contestar")
    elif 19 < hora_llamada < 23:
        print("No contestar")
