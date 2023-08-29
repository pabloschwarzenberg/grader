def buscarTodas(texto,caracter):
    #len(buscarTodas)
        


    resultado =[]
    largo = len(texto)
    lista = str
    
    for i in range(0, largo):
        if texto[i] == caracter:
            resultado.append(i)
            #print(largo, i)
            if i == 0:
                lista = str(i)
                #lista += " "
            if i > 0:
                lista += " "
                lista += str(i)
                
                
            #if i == largo:
             #   lista += str(i)
                
                
                
            #print(i)
            #resultado.append('')
        
    #print("uno")    
    #print(resultado)
    #print(buscarTodas)
    #i = 0 
    #lista = ()
    #while len(resultado) > i:
        #for i in range(0,len(resultado)):
        
        #lista += str(" ")
    #print(len(lista))    
    print(lista)
    
    return lista
    #pass

if __name__ == "__main__":
    
    texto =  str(input("Ingrese el texto --> "))  
    caracter =  str(input("Ingrese el caracter --> "))
    
    buscarTodas(texto,caracter)
    #print("dos")
    #print(resultado)
    #print(buscarTodas)
    #print(lista)
    
    pass

