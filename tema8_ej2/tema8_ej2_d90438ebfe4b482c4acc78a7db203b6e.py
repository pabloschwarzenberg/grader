def buscarTodas(a,b):
    lista = []
    x = ""
    for i in range(len(a)):
        if(a[i]==b):
            lista.append(i)
    if(len(lista)==0):
        return "no existe"
    
    for j in lista:
      j = str(j)
      if j != str(len(lista)):
        x += j
        if j != i:
          x += " "
      else:
        x += j
    x = x[:-1]

    return x
if __name__ == "__main__": 
  Var_1 = input()
  Var_2 = input()
  buscarTodas(Var_1 , Var_2)