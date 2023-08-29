modelo = str(input())
fix = str(input())

i = 0
while i <= len(fix):
    fix = list(fix)
    nro_guiones = modelo.find(fix[i], i) - i
    fix.insert(i, "_" * nro_guiones)
    fix = "".join(fix)
    i += (1 + abs(nro_guiones))
print(fix)
