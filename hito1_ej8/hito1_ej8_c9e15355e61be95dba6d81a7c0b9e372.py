#Descomponer un número
numero = int(input("Ingrese un número de 4 dígitos: "))
unidades = numero%10
numero = numero//10
decenas = numero%10
numero = numero//10
centenas = numero%10
numero = numero//10
umil = numero
print("Descomposición: ",umil," Unidades de Mil + ",centenas," Centenas + ",decenas," Decenas + ",unidades," Unidades")      