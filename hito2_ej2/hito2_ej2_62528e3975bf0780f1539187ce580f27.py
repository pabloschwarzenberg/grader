      def secuencia_valida(secuencia):
    for letra in secuencia:
        if not letra.lower() in "ACTG":
            return False
    return True


secuencia = "ACTG"
print("¿Es válida?")
print(secuencia_valida(secuencia))