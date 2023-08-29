def rot13(palabra):
    pass

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
 
def buscarTodas(a,b):

     m=[i for i,x in enumerate(a) if x==b]

     z=list(m)

     l=[]

     for i in z:

          l.append(str(i))

     w=" ".join(l)

     return w

