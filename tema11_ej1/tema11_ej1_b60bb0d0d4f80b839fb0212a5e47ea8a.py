def palindromo(ex):
    largo=len(ex)
    print(largo)
    if len(ex)==1:
        return True
    elif ex[0]==ex[largo-1]:
        ex=ex.strip(ex[0])
        return (palindromo(ex))
    if ex[0]!=ex[largo-1]:
        return False
if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           