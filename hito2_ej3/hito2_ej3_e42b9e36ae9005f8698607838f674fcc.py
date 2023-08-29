s = input('')
n = int(input(''))
largo = len(s)
substrings = []
eliminar = []
inicio = -1
fin = n - 1
while largo > fin:
    inicio += 1
    fin += 1
    if s[0:inicio].find(s[inicio:fin]) != -1:
        continue
    if s[fin:largo].find(s[inicio:fin]) != -1:
        continue
    if s[inicio:fin] in substrings:
        eliminar.append(s[inicio:fin])
    substrings.append(s[inicio:fin])
# Ahora eliminemos los repetidos
for i in eliminar:
    while i in substrings:
        substrings.remove(i)
if len(substrings) > 0:
    for i in substrings:
        print(i)
else:
    print('ninguna')
