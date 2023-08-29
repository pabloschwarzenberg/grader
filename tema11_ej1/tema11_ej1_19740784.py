def palindromo(palabra):
    word=list(palabra)
    palabra=[]
    palabra2=[]
    for letra in word:
        palabra.append(letra)
        palabra2.append(letra)
    palabra.reverse()
    print(palabra)
    print(palabra2)
    for i in range(len(word)):

      if palabra[i] != palabra2[i]:
        return False

    return True 


if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           