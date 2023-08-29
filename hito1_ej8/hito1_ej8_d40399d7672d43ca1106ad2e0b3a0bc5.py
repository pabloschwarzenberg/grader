#Descomponer un número
#Entrada

n = int(input("Ingrese un número de 4 digitos: "))

#Cáclculos

unidad_de_mil = n // 1000
centena = (n - (unidad_de_mil * 1000)) // 100
decena = (n - (unidad_de_mil * 1000 + centena * 100)) // 10
unidad = (n - (unidad_de_mil * 1000 + centena * 100 + decena *10)) 

print(unidad_de_mil,"M + ",centena,"C + ",decena,"D + ",unidad,"U")
