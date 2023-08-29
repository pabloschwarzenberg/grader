def palindromo(palabra):
    if palabra[0]==palabra[-1]:
        a=list(palabra)
        a.pop(0)
        a.pop(-1)
        ''.join(a)
        if len(a)==1 or len(a)==0:
            return True
        else:
            palindromo(a)
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           