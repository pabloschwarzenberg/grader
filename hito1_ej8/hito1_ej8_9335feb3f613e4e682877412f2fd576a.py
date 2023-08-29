#Descomponer un número
num=eval (input("Ingrese un número de 4 digitos \n "))
valor_miles=(num//1000) %10
valor_centenas=(num//100)%10
valor_decenas=(num//10)%10
valor_unidades=(num//1)%10

print (valor_miles,"M+",valor_centenas,"C+",valor_decenas,"D+",valor_unidades,"U",)