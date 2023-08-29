#Nota final

PT = input('PT: ')
PI = input('PI: ')
NE = input('NE: ')
PP = input('PP: ')
final = 0.3 * float(PT) + 0.3 * float(PI) + 0.3 * float(NE) + 0.1 * float(PP)
final = round(final,1)

print(final)