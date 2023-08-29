def palindromo(palabra):
    if len(palabra)==1:
        return True
    elif palabra[0]!=palabra[len(palabra)-1]:
        return False
    else:
        plabra=palabra[1:len(palabra)-1]
        return palindromo(palabra[1:len(palabra)-1])
  
           