def palindromo(s):
    l=len(s)
    if l<=1:
        return True
    if s[0]==s[-1] and palindromo(s[l:l-1])==True:
        return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           