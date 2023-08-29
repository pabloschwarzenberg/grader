def buscarTodas(a,b):
   lista=[]
   for i in range (0,len(a)):
       if a[i]==b:
         i=str(i)
         lista.append(i)
       posiciones=" ".join(lista)
   return posiciones

if __name__ == "__main__":
    a=input("ingrese palabra:")
    b=input("que letra busca?:")
           