gato = int(input(" ingrese el numero que desea convertir en binario: "))

perro = [int(d) for d in str(gato)]

n_binario = bin(gato)

print(" resultado = " + str(n_binario[2:]))