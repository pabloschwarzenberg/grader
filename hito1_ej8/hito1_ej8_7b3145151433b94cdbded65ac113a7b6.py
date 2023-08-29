numero = int(input('Ingrese un número de 4 cifras: '))
unidad=(numero%10)
decena= (numero%100)//10
centena = (numero//100)%10
milecima= numero//1000

print(f"{milecima}M + {centena}C + {decena}D + {unidad}U")
