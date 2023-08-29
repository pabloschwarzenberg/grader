def palindromo(s):
    a=len(s)-1
    sn=''
    while a>=0:
        sn+=s[a]
        a-=1
    if sn==s:
        return True
    else:
        return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           