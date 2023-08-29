#Descomponer un número
Numero = int(input("Ingrese un numero de hasta 4 digitos:"))
Unidades = Numero %10 
Decenas = (Numero //10) %10
Centenas = (Numero //100) %10
Miles = (Numero //1000) %10

print(Miles,"M +",Centenas,"C +",Decenas,"D +",Unidades,"U")
