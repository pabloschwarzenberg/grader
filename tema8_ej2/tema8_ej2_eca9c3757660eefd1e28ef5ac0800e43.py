def buscarTodas(a,b):
    indice=0
    string=""
    for letra in a:
        if letra in b:
            if indice<13:
               string+=str(indice)
               string+=" "
            if indice>=13:
               string+=str(indice)
               
        indice+=1
           
        
    return string
if __name__ == "__main__":
    a="tres tristes tigres"
    b="t"
    resultado=buscarTodas(a,b)
    
    print(resultado)
    pass        
