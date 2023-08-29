#Zodiaco

#ENTRADA

signos = ["sagitario", "acuario", "géminis" ,"piscis", "leo", "aries", "tauro", "capricornio", "cáncer", "virgo", "libra", "escorpio"]

fechas=[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

variables = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)

#PROCESAMIENTO
diaa = eval(input("Inserta el dia de tu cumpleaños : "))
fechas = eval(input("Inserta el mes de tu cumpleaños : "))
fechas = fechas - 1

#SALIDA

if fechas == 12:
   fechas == 0
   
elif diaa > variables [fechas]:
   fechas = fechas + 1
   
print (signos)