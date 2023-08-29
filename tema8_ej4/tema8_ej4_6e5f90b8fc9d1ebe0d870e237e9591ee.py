def rot13(palabra): 
  
        i=0
        palabra1=[]

        for i in range(i,len(palabra)):
                
                 if palabra[i] == "a":
                     palabra1.insert(i,'n')
                 elif palabra[i]== "n":
                     palabra1.insert(i,'a')
                 elif palabra[i]== "b":
                     palabra1.insert(i,'o')         

                 elif palabra[i]== "o":
                     palabra1.insert(i,'b')
                 elif palabra[i]== "c":
                     palabra1.insert(i,'p')
                 elif palabra[i]== "p":
                     palabra1.insert(i,'c')
                 elif palabra[i]== "d":
                     palabra1.insert(i,'q')
                 elif palabra[i]== "q":
                     palabra1.insert(i,'d')
                 elif palabra[i]== "e":
                     palabra1.insert(i,'r')
                 elif palabra[i]== "r":
                     palabra1.insert(i,'e')
                 elif palabra[i]== "f":
                     palabra1.insert(i,'s')
                 elif palabra[i]== "g":
                     palabra1.insert(i,'t')
                 elif palabra[i]== "t":
                     palabra1.insert(i,'g')
                 elif palabra[i]== "h":
                     palabra1.insert(i,'u')
                 elif palabra[i]== "u":
                     palabra1.insert(i,'h')
                 elif palabra[i]== "i":
                     palabra1.insert(i,'v')
                 elif palabra[i]== "v":
                     palabra1.insert(i,'i')
                 elif palabra[i]== "j":
                     palabra1.insert(i,'w')
                 elif palabra[i]== "w":
                     palabra1.insert(i,'j')
                 elif palabra[i]== "k":
                     palabra1.insert(i,'x')
                 elif palabra[i]== "x":
                     palabra1.insert(i,'k')
                 elif palabra[i]== "l":
                     palabra1.insert(i,'y')
                 elif palabra[i]== "y":
                     palabra1.insert(i,'l')
                 elif palabra[i]== "m":
                     palabra1.insert(i,'z')
                 elif palabra[i]== "z":
                     palabra1.insert(i,'m')
        codigo = "".join(str(x) for x in palabra1)
        return codigo

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           