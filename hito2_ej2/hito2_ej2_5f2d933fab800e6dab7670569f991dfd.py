def validate_sequence(sequence):
    # Convertir la secuencia a minúsculas
    sequence = sequence.lower()

    # Validar los caracteres de la secuencia
    for char in sequence:
        if char not in ['a', 'c', 't', 'g']:
            return False

    return True


# Obtener la entrada del usuario
sequence = input("Ingrese la secuencia de ADN: ")

# Validar la secuencia
if validate_sequence(sequence):
    print("secuencia correcta")
else:
    print("secuencia incorrecta")
