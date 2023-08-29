# completa el código de la función
def suma_divisores(a):
    i=1
    lista=[]
    suma=0
    suma_lista=[]
    while i<a:
        lista.append(i)
        i+=1
    
    for i in lista:
        if a%i==0 and i!=a:
            suma=suma+i
            suma_lista.append(i)
            i+=1
    if len(suma_lista)==1:
        return (str(suma)+","+"True")       
    else:
      return(str(suma)+","+"False")
           
            
     