x = eval(input())
lista = []
for y in range(x):
    c = x % (y+1)
    if c == 0:
        aux = (y+1)
        aux2 = x
        z = 0
        for a in range(y+1):
            c = (y+1) % (a+1)
            if c == 0:
                z += 1
        if z == 2:
            while (aux2 % aux) == 0:
                lista.append(y+1)
                aux2 //= aux
for g in lista:
  print(g)