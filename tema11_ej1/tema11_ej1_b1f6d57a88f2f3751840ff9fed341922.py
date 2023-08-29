def palindromo(a):
    a=list(a)
    l=[]
    for i in range(len(a)):
      l.insert(0,a[i])
    if str(l)==str(a):
      return True
    else:
      return False

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           