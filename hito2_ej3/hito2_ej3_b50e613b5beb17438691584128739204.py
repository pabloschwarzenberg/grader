def substring(n,s):
    lista = []
    todos = []
    i = 0
    h = n
    while len(s)> i :
        sub = s[i:h]
        if len(sub) == n:
            if sub not in todos:
                lista.append(sub)
                todos.append(sub)
            else:
                if sub in lista:
                    lista.remove(sub)
        i = i + 1
        h = h + 1
    if lista == []:
      lista = ['ninguna']

    return lista
b = input(":")
a = int(input(":"))

c = substring(a,b)

for linea in c:
  print(linea)