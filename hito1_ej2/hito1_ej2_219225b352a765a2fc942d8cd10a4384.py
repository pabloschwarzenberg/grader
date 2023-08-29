#Contestador de celular

#ENTRADA
numero = int(input("ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

#PROCESO
#variable que cambiara entre 0 y 1 siendo el 1 contestar y el 0 no contestar
contestar = 0
#variable que almacena el numero como una string para poder comparar 
num_comp = str(numero)
#Si la llamada ocurre entre 00:00 y 07:00
if ( 7 > hora > 0 ):
    contestar = 1
#Si ocurre antes de las 14:00 y si el número termina en 909.
elif (hora < 14) and (num_comp[5:8] == "909"):
    contestar = 1
#contestar entre 17:00 y 19:00, exceptuando un número que comienza por 877.
elif (19 > hora > 17) and (num_comp[0:3] != "877"):
    contestar = 1

#SALIDA
if (contestar == 1):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
                    