#Descomponer un número
numero = int(input("Ingrese 4 números: "))

unidad = numero % 10
decena = (numero % 10**2) // 10
centena = (numero % 10**3) // 10 ** 2
miles = (numero % 10**4) //10 ** 3

print("{}M + {}C + {}D + {}U".format(miles, centena, decena, unidad))