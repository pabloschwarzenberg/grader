#Descomponer un número
numero=int(input("Ingresar numero de 4 digitos: ")) 
unidad=numero//1%10 
decena=numero//10%10 
centena=numero//100%10 
mil=numero//1000 
print(mil,"M","+",centena,"C","+",decena,"D","+",unidad,"U")      