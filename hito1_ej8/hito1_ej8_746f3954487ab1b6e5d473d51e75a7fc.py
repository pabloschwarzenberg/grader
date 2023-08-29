#Descomponer un número
num = eval(input("Ingrese número: "))
unidad = num%10
decena = num%100//10
centena = num//100%10
milesima = num//10//10//10
print(unidad,"U+", decena,"D+", centena, "C+", milesima, "M")