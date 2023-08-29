def palindromo(palabra):
  lista1=[]
  lista2=[]
  for i in palabra:
    lista1.append(i)
  #lista2=lista1.reverse()
  for i in range(1,(len(palabra)+1)):
    letra=palabra[-i]
    lista2.append(letra)
  #print(lista1)
  #print(lista2)
  if lista1==lista2:
    return True
  else:
    return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))