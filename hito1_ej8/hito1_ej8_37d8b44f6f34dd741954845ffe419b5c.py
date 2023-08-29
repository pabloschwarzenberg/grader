#Descomponer un número
numCifras = int(input("Ingresa un número el cuál quieres descomponer ->"))

unidad = (numCifras//1) % 10

decena = (numCifras//10) % 10

centena = (numCifras // 100) % 10

unidadMil = (numCifras //1000)% 10

print("El número descompuesto es", unidadMil,"M +", centena,"C +", decena, "D +", unidad, "U")      