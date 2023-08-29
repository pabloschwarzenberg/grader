def rot13(palabra):
    pl = list(palabra) 
    l1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    l2 = ['n', 'o', 'p', 'k', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in range(len(palabra)): 
      if palabra[i] in l1: 
        pl.remove(palabra[i]) 
        pl.append(l2[l1.index(palabra[i])])   
      else:
        pl.remove(palabra[i])
        pl.append(l1[l2.index(palabra[i])])
    return (''.join(pl))

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           