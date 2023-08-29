secuencia = input("Ingrese la secuencia de ADN: ")
secuencia = secuencia.upper()  # Convertir la secuencia a mayúsculas

valida = True

for nucleotido in secuencia:
    if nucleotido not in ['A', 'C', 'T', 'G']:
        valida = False
        break

if valida:
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
    
#FIN