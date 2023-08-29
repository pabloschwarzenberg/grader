#Descomponer un número
numero=int(input("escriba un numero "))
milesima = numero//1000
centesima = numero//100%10
decima = numero//10%10
unidad = numero%10
print(milesima,"M+",centesima,"C+",decima,"D+",unidad,"U")