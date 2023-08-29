def palindromo(palabra):
  lista_1=list(palabra)
  a=lista_1[::-1]
  i=0
  for u in range(len(a)):
    if a[u]==lista_1[u]:
        i=i+1
    else:
        return False
  if i==len(palabra):
    return True
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           