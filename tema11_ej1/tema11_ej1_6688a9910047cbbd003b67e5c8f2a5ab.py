def palindromo(palabra,contador = 0):
    if len(palabra) == 1:
        return palabra[-1]
    else:
         resto = palindromo(palabra[0:-1],1)
         if contador == 0:
             if palabra[-1] + resto == palabra:
                 return True
             else:
                return False
         return palabra[-1] + resto

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           