# Senadora.

#datos.
#votos totales en cada comuna.
total_comuna1 = input("Ingrese el total de votos de Comuna 1: ")
total_comuna2 = input("Ingrese el total de votos de Comuna 2: ")
total_comuna3 = input("Ingrese el total de votos de Comuna 3: ")
print(15*"-")

#validacion de datos.
try:
    #redondeo de numeros.
    total_comuna1 = int(total_comuna1)
    total_comuna2 = int(total_comuna2)
    total_comuna3 = int(total_comuna3)

    #confirmacion de votos.
    print("El total de votos en comuna 1 es: ", total_comuna1)
    print("El total de votos en comuna 2 es: ", total_comuna2)
    print("El total de votos en comuna 3 es: ", total_comuna3)
    print(15*"-")
except ValueError:
    print("error al ingresar el total de datos.")
    print(15*"-")

#total de votos en provincia.
total_provincia = total_comuna1 + total_comuna2 + total_comuna3

#cantidad de votos por comuna.
votos_comuna1 = input("ingrese la cantidad de votos de la comuna 1: ")
votos_comuna2 = input("ingrese la cantidad de votos de la comuna 2: ")
votos_comuna3 = input("ingrese la cantidad de votos de la comuna 3: ")
print(15*"-")


#validacion de votos.
try:
    #redondeo de numeros.
    votos_comuna1 = int(votos_comuna1)
    votos_comuna2 = int(votos_comuna2)
    votos_comuna3 = int(votos_comuna3)

    #confirmacion de votos.
    print("La Cantidad de votos en la comuna 1 es: ", votos_comuna1)
    print("La Cantidad de votos en la comuna 2 es: ", votos_comuna2)
    print("La Cantidad de votos en la comuna 3 es: ", votos_comuna3)
    print(15*"-")
except ValueError:
    print("error al ingresar la cantidad de votos.")
    print(15*"-")

#porcentaje total comunas.
pt100_comuna1 = (total_comuna1 * 1) #100% del total de votos.
pt80_comuna1 = total_comuna1 - (total_comuna1 * 0.2) #80% del total de votos.

pt100_comuna2 = (total_comuna2 *1) #100% 
pt80_comuna2 = total_comuna2 - (total_comuna2 * 0.2) #80% 

pt100_comuna3 = (total_comuna3 * 1) #100%
pt80_comuna3 = total_comuna3 - (total_comuna3 * 0.2) #80%

#porcentaje provincia
pt100_provincia = total_provincia * 1 #100%
pt70_provincia = total_provincia - (total_provincia * 0.3) #70%
pt40_provincia = total_provincia - (total_provincia * 0.6) #20%

#suma de votos de dos comunas.
suma_comuna12 = votos_comuna1 + votos_comuna2
suma_comuna13 = votos_comuna1 + votos_comuna3
suma_comuna23 = votos_comuna2 + votos_comuna3

#suma de votos en tres comunas.
suma_comuna123 = votos_comuna1 + votos_comuna2 + votos_comuna3

#ganar por 80% en alguna comuna.
if votos_comuna1 >= pt80_comuna1 or votos_comuna2 >= pt80_comuna2 or votos_comuna3 >= pt80_comuna3:
    print("senadora electa")

#ganar por la suma de 2 comunas igual a 70% de provincia.  // provincia = 300, pt70= 210, comuna = 70
elif suma_comuna12 >= pt70_provincia or suma_comuna13 >= pt70_provincia or suma_comuna23 >= pt70_provincia:
    print("senadora electa")

#ganar por un total de 40% en provincia. // provincia = 300, pt40 = 120, comuna = 40
elif suma_comuna123 >= pt40_provincia:
    print("senadora electa")
else:
    print("candidata perdedora")