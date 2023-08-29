#Descomponer un número
print("descomponga un número en unidades, decenas, centenas y unidades de mil, ")
print("a partir de un número entero de 4 cifras ingresado por el usuario")

#declaracion de variables y constantes
numero=int(input("Ingrese el número entero de 4 cifras= "))
numero_original=numero

#operaciones

unidades=numero%10
numero=numero//10
decenas=numero%10
numero=numero//10
centenas=numero%10
numero=numero//10
unidadesMil=numero%10

#mostrar resultados
print("Descomposición:" ,unidadesMil,"M +" ,centenas,"C +",decenas,"D +" ,unidades,"U")
#fin del programa