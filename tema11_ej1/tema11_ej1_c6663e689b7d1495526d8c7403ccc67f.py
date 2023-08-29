def reversa(palabra):
    if len(palabra)==1:
        return palabra
    else:
        nueva=palabra[:-1]
        return palabra[-1]+reversa(nueva)
def palindromo(palabra):
    if reversa(palabra)==palabra:
        return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           