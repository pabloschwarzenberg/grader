#Contestador de celular
phone = int(input("Ingrese numero telefonico: "))
hour = int(input("Ingrese hora de la llamada: "))

# Verificar si la llamada ocurre entre 00:00 y 07:00
if hour >= 0 and hour <= 7:
    print("CONTESTAR")
# Verificar si la llamada ocurre antes de las 14:00 y el número termina en 909
elif hour < 14 and phone % 1000 == 909:
    print("CONTESTAR")
# Verificar si la llamada ocurre durante la tarde y el número comienza por 877
elif hour >= 17 and hour <= 19 and phone // 100000 == 877:
    print("NO CONTESTAR")
# En cualquier otro caso, no contestar la llamada
else:
    print("NO CONTESTAR")
