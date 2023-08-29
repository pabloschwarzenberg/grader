def palindromo(palabra):
  if len(palabra)==1:
    return True
  elif len(palabra)==2:
    if palabra[0] == palabra[1]:
     return True
    else:
      return False
  
  elif len(palabra) != 1 or len(palabra) != 2:
    a = list(palabra)
    cabeza = a[0]
    cola = a[-1]
    if cabeza==cola:
      a.pop(0)
      a.pop(-1)
      palabra = "".join(a)
      return palindromo(palabra)

    else:
       return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           