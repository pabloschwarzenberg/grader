def palindromo(n):
    l=len(n)
    if l<=1:
        return True
    if n[0]==n[-1]:
        if palindromo(n[1:l-1])==True:
            return True
        else:
            return False
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           