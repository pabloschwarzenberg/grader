# Programa para ordenar números del menor al mayor

prinum = int (input("Ingresa el primero número: "))
segnum = int (input("Ingresa el segundo número "))
ternum = int (input("Ingresa el tercer número "))

minnum = min (prinum, segnum, ternum)
maxnum = max (prinum, segnum, ternum)
mednum = (prinum + segnum + ternum) - minnum - maxnum

print ("Sus números ordenados son: " + str(minnum) + "," + str(mednum) + "," + str(maxnum))