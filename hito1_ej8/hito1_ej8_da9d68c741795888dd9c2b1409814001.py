#Descomponer un número
N=eval (input("Ingrese un número de 4 digitos \n "))
valor_miles=(N//1000) %10
valor_centenas=(N//100)%10
valor_decenas=(N//10)%10
valor_unidades=(N//1)%10

print (valor_miles,"M+",valor_centenas,"C+",valor_decenas,"D+",valor_unidades,"U",)