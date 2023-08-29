def buscarTodas(a,b):
     lista=[i for i,x in enumerate(a) if x==b]

     end=list(lista)

     leng=[]

     for y in end:

          leng.append(str(y))

     res=" ".join(leng)

     return res  

if __name__ == "__main__":
    pass
           