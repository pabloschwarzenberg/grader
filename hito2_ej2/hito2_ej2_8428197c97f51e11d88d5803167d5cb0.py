def validate_sequence(sequence):
    valid = set('ACTG')
    sequence = sequence.upper()
    if set(sequence).issubset(valid):
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")      