def is_valid_dna(dna):
  valid = True
  for nuc in dna:
    if nuc not in ['A', 'C', 'G', 'T']:
       valid = False
  return valid
  
sequence = input()
if is_valid_dna(sequence):
  print('secuencia correcta')
else:
  print('secuencia incorrecta')