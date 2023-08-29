#Descomponer un número
numero = eval(input("Ingrese número de 4 cifras: "))

valor_miles = (numero//1000)%10
valor_centenas = (numero//100)%10
valor_decenas = (numero//10)%10
valor_unidad = (numero//1)%10

print("Unidad de Mil: ",valor_miles)
print("Centena: ",valor_centenas)
print("Decena: ",valor_decenas)
print("Unidad: ", valor_unidad)

print("Resultado: ",valor_miles,"M + ",valor_centenas,"C + ",valor_decenas,"D + ",valor_unidad,"U")
 
resultado = str(valor_miles) + "M + " + str(valor_centenas) + "C + " + str(valor_decenas) + "D + " + str(valor_unidad) + "U"
print("Resultado: ",resultado)
      