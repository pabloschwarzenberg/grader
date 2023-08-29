#Para 1230
numero = int(input("Ingrese su valor"))
unidad = numero%10
decena = (numero%100)//10
centena = (numero%1000)//100
unidadDeMil = numero//1000
print(unidadDeMil, "M +", centena, "C +", decena, "D +", unidad, "U")#Para 36
numero2 = 36
unidadA = numero2%10
decenaA = (numero2%100)//10
print(decenaA, "D +", unidadA, "U")