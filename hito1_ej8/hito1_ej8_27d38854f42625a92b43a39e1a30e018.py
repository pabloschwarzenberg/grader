#Descomponer un número
numero=int(input("ingrese un numero de 4 digitos maximo:"))

		
millares=(numero//1000)
centenas=((numero-(millares*1000))//100)
decenas=((numero-(millares*1000 + centenas*100))//10)
unidades=(numero-(millares*1000 + centenas*100 + decenas*10 ))

print(millares,"M","+",centenas,"C","+",decenas,"D","+",unidades,"U");
