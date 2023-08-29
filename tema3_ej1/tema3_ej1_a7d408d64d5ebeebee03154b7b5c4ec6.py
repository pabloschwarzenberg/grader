def suma_divisores(a):
    suma=[]
    i=1
    while i<a:
        if a%i==0:
            suma.append(i)
            print(i)
        i+=1
    b=sum(suma)
    if b==1:
        return (b,True)
    else:
        return (b,False)

  
if __name__ == "__main__":
  numero=int(input())
  print(suma_divisores(numero))
