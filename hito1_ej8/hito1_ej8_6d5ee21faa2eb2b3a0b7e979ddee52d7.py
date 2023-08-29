#Descomponer un número
numero = eval(input("ingrese numero de 4 cifras: "))

valor_miles = (numero // 1000)% 10
valor_centenas = (numero // 100) % 10
valor_decenas = (numero // 10) % 10
valor_unidades = (numero // 1) % 10

print("resultado: ", valor_miles,"M + ",valor_centenas,"C + ",valor_decenas,"D + ",valor_unidades,"U")