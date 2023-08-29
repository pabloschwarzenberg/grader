def palindromo(palabra):
  if len(palabra)==0 or len(palabra)==1:
    return True
  else:
    lista=[]
    for i in palabra:
      lista.append(i) 
    if palabra[0]==palabra[(len(palabra)-1)]:
      lista.pop(len(palabra)-1)  
      lista.pop(0)
      palabra="".join(lista)
      return palindromo(palabra)
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           