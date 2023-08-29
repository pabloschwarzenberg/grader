def evaluar(secuencia,largo):
  l = []
  l_borrados = []
  l_sirven = []
  i = 0
  while i <= len(secuencia)-largo:
    a = ""
    for j in range(largo):
      a = a + secuencia[i+j]      
    l.append(a)
    i+=1
  i = 0
  while i < len(l):
      while l.count(l[i]) != 1:
          l_borrados.append(l[i])
          l.pop(i)
      if l.count(l[i]) == 1 and l[i] not in l_borrados:
          l_sirven.append(l[i])
      i+=1
  if l_sirven == []:
      print("niguna")
  else:
      i=0
      while i < len(l_sirven):
          print(l_sirven[i].lower())
          i+=1

if __name__ == "__main__":
  string = str.upper(input())
  n = int(input())
  evaluar(string,n)