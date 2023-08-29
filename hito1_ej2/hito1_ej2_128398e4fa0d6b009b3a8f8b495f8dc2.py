#Contestador de celular
# Entradas
phone = str(int(input("Ingrese un numero telefonico: ")))
hour = int(input("Ingrese la hora de la llamada: "))

# Procesamiento
# Comienzo del numero
one = phone[0] + phone[1] + phone[2]
# Termino del numero
two = phone[-3] + phone[-2] + phone[-1]

# Condiciones para contestar o no
if 8 < len(phone):
    print("Ingrese un numero de 8 digitos")
elif 23 < hour:
    print("Ingrese una hora entre las 00:00 y 23:00")
elif 0 < hour < 7:
    print("CONTESTAR")
elif 7 < hour < 14:
    if two == "909":
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif 14 < hour < 19:
    if 17 < hour < 19 and one == "877":
        print("NO CONTESTAR")
    elif 17 < hour < 19:
        print("CONTESTAR")
    elif 14 < hour < 17:
        print("NO CONTESTAR")
elif 19 < hour:
    print("NO CONTESTAR")     