#Descomponer un número
# Entradas --------

número = int(input("Ingrese un número de 4 cifras: "))
# Variables-------------------------------------------------------

milesima = int(número//1000)
centesima = int((número - (milesima*1000))//100)
decima = int((número - (milesima*1000 + centesima*100))//10)
unidad = int((número - ( milesima*1000 + centesima*100 + decima*10)))

if número//1000 >= 1:
    m = milesima + centesima + decima + unidad

# Salida--------------------------------------------------------------------------
print("Descomposición: ", milesima, "M +", centesima, "C +", decima, "D +", unidad, "U.")