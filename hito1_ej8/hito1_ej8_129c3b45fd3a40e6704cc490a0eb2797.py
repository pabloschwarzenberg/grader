#Descomponer un número
numero = eval(input("ingresa un numero de 4 digitos: "))
unidad = numero%10
decena = (numero%100)//10
centena = (numero%1000)//100
unidadDeMil = numero//1000
print(unidadDeMil,"M + ",centena,"C + ",decena,"D + ",unidad,"U + ")