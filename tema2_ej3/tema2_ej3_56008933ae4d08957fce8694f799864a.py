def numero_perfecto(a):
     d=1
     lista=[]
     while d<a:
       if a%d==0:
          lista.append(d)  
       d=d+1

     if sum(lista)==a:
         return True
     else:
         return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           