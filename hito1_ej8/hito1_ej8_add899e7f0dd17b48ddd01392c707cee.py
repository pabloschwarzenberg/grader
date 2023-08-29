#Descomponer un número
print("Escribe un numero: ")

int(miles=(numero/1000))
int(centenas=(numero-(miles*1000))/100)
int(decenas=(numero-((miles*1000)+(centenas*100)))/10)
int(unidades=(numero-((miles*1000)+(centenas*100)+(decenas*10)))

print("Miles = %i/n", miles)
print("Centenas = %i/n", centenas)
print("Decenas = %i/n", decenas)
print("Unidades = %i/n", unidades)