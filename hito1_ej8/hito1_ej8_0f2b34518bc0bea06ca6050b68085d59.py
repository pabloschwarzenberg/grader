#Descomponer un número
# Entrada

a = float(input("Ingresa un valor de 4 cifras: "))


# Calculos

unidad_de_mil = int(a//1000)

n_hasta_la_centena = a%1000

centena = int(n_hasta_la_centena//100)

n_hasta_la_decena = n_hasta_la_centena%100

decena = int(n_hasta_la_decena//10)

n_hasta_la_unidad = n_hasta_la_decena%10

unidad = int(n_hasta_la_unidad//1)

# Salida

print(unidad_de_mil,"M + ",centena,"C + ",decena,"D + ",unidad,"U")
    
print("Fin.")