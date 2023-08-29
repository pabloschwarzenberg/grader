sequence = input("Ingrese la secuencia: ")
valid_letters = {'A', 'C', 'T', 'G'}
sequence_set = set(sequence.upper())
if sequence_set.issubset(valid_letters):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")