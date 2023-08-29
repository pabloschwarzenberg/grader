#Descomponer un número
n = int(input("indicar un número que contenga unidad, decena, centena y miles : "))
unidad = n%10
n = n//10
decena = n%10
n = n//10
centena = n%10
n = n//10
miles = n%10
n = n//10
print(miles,"M +",centena,"c +",decena,"D +", unidad,"U +")            