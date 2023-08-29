rut = input('Rut: ')
sum_comp = sum([int(a) * int(b) for a, b in zip(str(rut).zfill(8), '32765432')])
verif = 11 - sum_comp % 11
verif = {10: 'K', 11: '0'}.get(verif, str(verif))
print("dv=" + verif)
