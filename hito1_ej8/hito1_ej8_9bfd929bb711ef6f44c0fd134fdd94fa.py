#Descomponer un número
n = int(input("ingrese un número de máximo 4 cifras: "))
unidad = (n//1)%10
decena = (n//10)%10
centena = (n//100)%10
mil = (n//1000)%10

print("la descomposición del número", n, "es: ", mil,"M +",centena, "C+", decena,"D+",unidad,"u"  )