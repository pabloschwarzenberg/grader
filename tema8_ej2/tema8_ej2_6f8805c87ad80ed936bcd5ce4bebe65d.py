def buscarTodas(a,b):
    global lista
    lxpal=1
    while lxpal>0:
        x= a.find(b)
        lxpal= a.count(b)
        
        c= lista.append[x]
        print(lista)
lista=[] 

if __name__ == "__main__":
    a= str(input("Ingrese texto: "))
    b= str(input("Ingrese string que desea encontrar: "))
    buscarTodas(a,b)
lista=[]    
      