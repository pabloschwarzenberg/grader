#Descomponer un número
numero = eval(input("Ingrese numero a descomponer: "))

milesima = (numero//1000) %10
centena = (numero//100) %10
decima = (numero//10) %10
unidad = (numero//1) %10

print("El resultado es: ",milesima,"M +",centena,"C +",decima,"D +",unidad,"U")
     