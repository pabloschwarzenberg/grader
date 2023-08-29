def palindromo(palabra):
    lista = list(palabra)
    if lista[0] != lista[-1]:
         return False
    if len(lista) <= 1:
        return True
    elif len(lista) > 1:
         lista.pop(0)
         lista.pop(-1)
         return palindromo(lista)

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           