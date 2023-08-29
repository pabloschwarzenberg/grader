def buscarTodas(a,b):
    td = []
    for i in range(len(a)):
        if(a[i]==b):
            td.append(i)
    if(len(td)==0):
        return "no existe"
    
    return td 
    
if __name__=="__main__":
  print(buscarTodas("tres tristes tigres","t"))   
 


