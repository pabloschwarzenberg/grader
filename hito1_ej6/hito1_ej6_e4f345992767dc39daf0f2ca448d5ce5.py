#Ordenar tres números
p = int(input("escriba el primer número uwu: "))
o = int(input("escriba el segundo número uwu: "))
i = int(input("escriba el tercer número uwu: "))

q = min(p, o, i)
e = max(p, o, i)
w = (p + o + i) - q - e

print("Los número ordenados son *redoble de tambores*: {}, {}, {}" .format(q, w, e))
