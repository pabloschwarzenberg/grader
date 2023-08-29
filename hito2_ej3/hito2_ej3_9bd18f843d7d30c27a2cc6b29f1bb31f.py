adn = input('secuencia: ')
n = int(input('largo de la secuencia: '))
L = [ ]
for i in range(0,(len(adn)-n+1)):
    c = 0
    x = adn[i:n+i]
    for k in range(0,(len(adn)-n+1)):
        y = adn[k:n+k]
        if x == y:
            c += 1
    if c == 1:
        L.append(x)

if len(L) != 0:
    for m in L:
        print(m)
else:
    print('ninguna')