def primo(num):
  if(num > 1):
    for i in range(2, int(num * 0.5) + 1):
      if(num % i == 0):
        return False
  else:
    return False
  return True
def hecho(num):
  listprimo=[]
  listdivisores=[]
  if(num > 1):
    if(num == 2):
      listprimo.append(2)

    for i in range(2, int(num * 0.5) + 1):
      i_int=int(i)
      if(primo(i_int) and num % i_int == 0):
        listprimo.append(i_int)

    for j in range(1, num + 1):
      j_int=int(j)
      if(num % j_int == 0):
        listdivisores.append(j)
    listdef = list(listdivisores and listprimo)

  else:
    pass
  
  return listdef

n=int(input("Ingrese un número: "))
x= hecho(n)
for i in x:
  print(i)
