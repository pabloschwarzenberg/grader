ai = int(input("Ingresar primer número: "))
bi = int(input("Ingresar primer segundo: "))
ci = int(input("Ingresar primer tercer: "))

A = min(ai, bi, ci)
C = max(ai, bi, ci)
B = (ai + bi + ci) - A - C
print("Resultado: {}, {}, {}" .format(A, B, C))