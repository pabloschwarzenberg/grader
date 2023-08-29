#Ordenar tres números
lista =[]
lista.append(int(input("")))
lista.append(int(input("")))
lista.append(int(input("")))
a = sorted(lista)
txt= ""
for i in range(len(a)):
  if i!= len(a)-1:
    txt = txt+ str(a[i]) +","
  else:
    txt = txt +str(a[i])
print(txt)