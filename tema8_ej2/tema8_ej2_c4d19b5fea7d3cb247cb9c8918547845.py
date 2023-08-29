def buscarTodas(a,b):
    j = a.index(b)
    listo = []
    if (a.count(b) > 1):
        
        for i in range(j, len(a)):
            no = a.index(b, i)
            k = no in listo
            
            if(k == False):
                listo.append(no)
                
                if(len(listo) == a.count(b)):
                    
                    break
                
                elif(len(listo) == a.count(b)):
                
                    break
                
                else:
                
                    continue
                    
    s=str(listo)
    s=s.strip("[")
    s=s.strip("]")
    s = s.replace(",","")
    

    return s
                
            
            

if __name__ == "__main__":
    a = str(input("Que palabra quiere ingresar:"))
    b = str(input("Que termino busca:"))
    
           