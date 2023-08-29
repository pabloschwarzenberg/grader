def palindromo(palabra):
    palabral=list(palabra)
    copia=[]
    for i in range(len(palabral)):
        a=palabral[i]
        copia.insert(0,a)
    if palabral==copia:
        return True
    elif palabral!=copia:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           