#Descomponer un número
numero=int(input("Ingrese el numero que quiere descomponer: "))

miles=(numero//1000)%10
centena=(numero//100)%10
decena=(numero//10)%10
unidad=(numero//1)%10

print("Para el numero", numero, "posee:", miles,"M +",centena,"C +",decena,"D +",unidad,"U")