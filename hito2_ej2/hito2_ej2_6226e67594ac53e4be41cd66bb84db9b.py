
genome = input('Inserta el genoma aqui: ').upper()
gen = set(genome)
pat = set(['A', 'C', 'G', 'T'])

if gen - pat:
    print('Secuencia incorrecta')
else:
    print('Secuencia correcta')