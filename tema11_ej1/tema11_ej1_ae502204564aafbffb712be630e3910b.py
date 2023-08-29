def palindromo(palabra):
     palabra1=list(palabra)
     palabra1.reverse()
     palabra1="".join(palabra1)
     if palabra1==palabra:
       return True
     else:
       return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           