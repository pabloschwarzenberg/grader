def buscarTodas(a,b):
    l = []
    i = 0
    a = a.replace(b,"_")
    for b in a:
      if b == "_":
        l.append(str(i))
      i += 1
    return " ".join(l)
           