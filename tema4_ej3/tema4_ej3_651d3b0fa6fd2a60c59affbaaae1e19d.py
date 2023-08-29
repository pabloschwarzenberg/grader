def jerigonzo(string):
    u=len(string)
    vocales=["a","e","i","o","u"]
    n=0
    string=list(string)
    while n<5:
      v=vocales[n]
      a=string.count(v)
      j=0
      u=0
      while j<a:
        if vocales[n] in string:
          b=string.index(vocales[n],u)
        string.insert(b+1,"p")
        string.insert(b+2,vocales[n])
        u=b+3
        j=j+1
      n=n+1
    string="".join(string) 
    return string

if __name__ == "__main__":
    pass
         