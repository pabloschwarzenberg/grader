def buscarTodas(a,b):
    a=str(a)
    c=len(a)
    b=str(b)
    contador=""
    
    for i in range(0,c):
        if a[i]==b:
            contador+=str(i)
            contador+=" "
    
    contador=contador.strip()
    
    return contador
      

if __name__ == "__main__":
   a=input()
   b=input()
   print(buscarTodas(a,b))
           