      def secuencia_valida(secuencia):
    for letra in secuencia:
        if not letra.lower() in "actg":
            return False
    return True
# Probar
secuencia = input("Ingrese la secuencia: "))
if secuencia = "ACTGactgGCTA"
print("Entonces, ¿la secuencia es válida?")
print(secuencia_valida(secuencia))
