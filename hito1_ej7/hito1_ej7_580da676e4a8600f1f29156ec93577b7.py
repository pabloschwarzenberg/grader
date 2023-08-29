#Zodiaco
x = ["Capricornio", "Acuario", "Picis", "Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario"]
y = [22, 20, 19, 21, 20, 21, 21, 23, 23, 23, 23, 22]

a = int(input("Ingrese su dia de nacimiento: "))
z = int(input("Ingrese su mes de nacimiento: "))

z = z - 1
if a > y [z]:
   z = z + 1
if z == 12:
    z = 0
print("Su signo del Zodico es", x[z])
