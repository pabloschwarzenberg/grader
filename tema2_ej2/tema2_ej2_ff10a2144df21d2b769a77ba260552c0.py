def amigos(a,b):
    i=1
    suma=0
    l=[]
    while i<a:
        if a%i==0:
            suma=suma+i
            l.append(i)
            i=i+1
        else:
            i=i+1
    if suma==b:
        return True
    else:
        return False
        
if __name__=="__main__":
  a=int(input())
  b=int(input())
  print(amigos(a,b))
  
        

