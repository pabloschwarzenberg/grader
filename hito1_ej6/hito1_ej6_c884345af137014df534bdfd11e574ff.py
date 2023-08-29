#Ordenar tres números
varAux_1 = 0
varAux_2 = 0
varAux_3 = 0

primerNumero = int(input("Ingrese primer numero: "))
segundoNumero = int(input("Ingrese segundo numero: "))
tercerNumero = int(input("Ingrese tercer numero: "))

varAux_1 = min(primerNumero, segundoNumero, tercerNumero)
varAux_2 = max(primerNumero, segundoNumero, tercerNumero)
varAux_3 = (((primerNumero + segundoNumero + tercerNumero) - varAux_1) - varAux_2)

print("Los numeros ordenados son:", varAux_1, varAux_3, varAux_2)