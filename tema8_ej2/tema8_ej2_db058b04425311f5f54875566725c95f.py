def buscarTodas(a,b):
  lista =[]
  t=" "
  for i in range(len(a)):
    if (a[i]==b):
      lista.append(str(b))
      l=t.join(lista)
      if (len(lista)==0):
        return "no existe"
       