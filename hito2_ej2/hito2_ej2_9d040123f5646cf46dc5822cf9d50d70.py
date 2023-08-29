def secuencia_valida(secuencia, gen):
    for letra in secuencia:
        if letra.lower() in gen:
            return "secuencia correcta"
        elif letra.lower() not in gen:
            return "secuencia incorrecta"
            
gen = "actg"
secuencia = input("Ingrese la secuencia: ")

print(secuencia_valida(secuencia, gen))

