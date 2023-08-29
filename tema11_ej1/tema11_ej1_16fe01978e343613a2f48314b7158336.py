def palindromo(palabra):
    lista = []
    p = 0
    for letra in palabra:
        lista.append(letra)
        
    if len(lista)%2 == 0:
        return False
    else:
        while len(lista)>1:
            
            if lista[0] == lista[-1]:
                p+=1

            lista.remove(lista[0])
            lista.remove(lista[-1])
            
        
        if p == len(palabra)//2:
            return True
        else:
            return False
        palindromo(palabra)

            
         

if __name__=="__main__":
    
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           