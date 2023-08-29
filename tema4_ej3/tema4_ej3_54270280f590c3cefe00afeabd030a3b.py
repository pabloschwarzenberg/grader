def jerigonzo(string):
    
    string = "estamos programando"
    string = string.strip()
    
    lista = []

    for letra in string:
        if letra in "aeiou":
            lista.append(letra+"p"+letra)
        else:
            lista.append(letra)

    resultado = "".join(lista)
    return resultado
       
      

    
  

       
            


            


            

if __name__ == "__main__":
    pass
         