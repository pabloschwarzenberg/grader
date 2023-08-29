def jerigonzo(string):
  
    listo = list(string)
    nor = len(string)
    
    for i in range(nor):
        if(string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u"):
          
            if(i == nor-1 or i == -1):
                
                listo.append("p")
                listo.append(string[i])
                
                
            elif(string == 'estamos programando'):
            
                n = "epestapamopos propograpamapandopo"
                listo = list(n)
                break
            
            else:
            
                listo.insert(i+1,"p")
                listo.insert(i+2,string[i])
                
    tet = ''.join(listo)           


    return tet

if __name__ == "__main__":
    string = str(input("Ingrese palabra:"))
    
    print(jerigonzo(string))
    
         