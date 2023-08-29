def is_valid_genome_sequence(sequence):

    valid_chars = {'A', 'C', 'T', 'G'}

    sequence = sequence.upper()

 

    for char in sequence:

        if char not in valid_chars:

            return False

 

    return True

 

# Obtener la secuencia de ADN desde la entrada del usuario

sequence = input("Ingresar secuencia de ADN: ")

 

# Validar la secuencia del genoma

if is_valid_genome_sequence(sequence):

    print("secuencia correcta")

else:

    print("secuencia incorrecta")
     