def secuencia_valida(secuencia):
    for letra in secuencia:
        if not letra.lower() in "actg":
            return secuencia incorrecta
    return secuencia correcta

secuencia = "ACTGactgGCTA"
print(secuencia_valida(secuencia))      