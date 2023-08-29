#Descomponer un número
n = int(input("ingrese numero a descomponer de 4 digitos o mneos: "))
milesima = n//1000
centena =( n - milesima*1000) //100
decima = (n - milesima*1000-centena*100)//10
unidad = (n -milesima*1000-centena*100-decima*10)//1
print(milesima,"M + ",centena,"C + ",decima,"D +",unidad,"U")      