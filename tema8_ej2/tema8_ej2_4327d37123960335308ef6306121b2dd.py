def buscarTodas(a,b):
    a1=list(a)
    print(a1)
    n=len(a1)
    string=""
    cont = 0
    for i in a1:
      if i.lower()==b:
        string+=str(cont)
        string+=" "
      cont += 1
    return string.strip()