def rot13(palabra):
    lis = []
    
    for i in range(65, 91):
        lis.append(i)
        
    for i in range(97, 123):
        lis.append(i)
        
    lisrot = []
    
    for i in range(len(lis)):
        if i < 26 and i + 13 < 26:
            lisrot.append(lis[i + 13])
        elif i < 26:
            lisrot.append(lis[i - 13])
        elif i + 13 < 52:
            lisrot.append(lis[i + 13])
        else:
            lisrot.append(lis[i - 13])
        
    lisp = list(palabra)
    for i in range(len(palabra)):
        lisp[i] = ord(lisp[i])
    
    for i in range(len(lisp)):
        let = lisp[i]
        
        if let in lis:
          ind = lis.index(let)
          lisp[i] = lisrot[ind]
          
    for i in range(len(lisp)):
        lisp[i] = chr(lisp[i])
          
    palabra = "".join(map(str, lisp))
    
    
    return palabra

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           