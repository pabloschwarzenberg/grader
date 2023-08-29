def es_primo(x):
    c=x-1
    if x==2:
        return True
    elif x==1:
        return False
    else:
        b=x-1
        while b>1:
            if x%b==0:
                return False
            b=b-1
            c=c-1
            if c==1:
                return True

if __name__=="__main__":
  a=int(input("numero"))
  print(es_primo(a))