# Ingreso de secuencia
secuencia = input("Ingrese secuencia: ")
secuencia = secuencia.upper()
secuencia_en_lista = list(secuencia)

# Verificacion
for i in secuencia:
    if i != "A" or i != "G" or i != "T" or i != "C":
        print("Secuencia incorrecta")
    else:
        print("Secuencia correcta")