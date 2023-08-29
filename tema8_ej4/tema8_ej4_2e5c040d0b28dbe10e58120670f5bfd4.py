def rot13(palabra):
    lista="a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z"
    desplazamiento=1
    rolt13=""
    for car in palabra:
        if car in lista:
             rolt13 +=lista[(lista.index(car)+desplazamiento%(len(lista)))]
        else:
          rolt13+=car
   
    return rolt13


if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           