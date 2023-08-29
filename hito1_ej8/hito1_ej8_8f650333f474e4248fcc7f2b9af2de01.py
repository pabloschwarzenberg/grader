#Descomponer un número
a = input()
j = []
c = -1
for n in a:
    c += 1
    j.append(n)

if c == 0:
    print(j[0], "u")
elif c == 1:
    print(j[0], "d", "+", j[1], "u")
elif c == 2:
    print(j[0], "c", "+", j[1], "d", "+", j[2], 'u')
elif c == 3:
    print(j[0], "m", "+", j[1], "c", "+", j[2], 'd', "+", j[3], "u")     