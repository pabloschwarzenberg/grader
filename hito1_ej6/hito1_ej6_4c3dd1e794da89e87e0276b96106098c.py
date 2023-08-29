#Ordenar tres números
      x=int(input("escriba un numero"))
      y=int(input("escriba otro numero"))
      z=int(input("escriba otro numero"))
      
     a=min(x,y,z)
     b=max(x,y,z)
     c=(x+y+z)-a-b
     print("los numeros ordenados son", (a,c,b)