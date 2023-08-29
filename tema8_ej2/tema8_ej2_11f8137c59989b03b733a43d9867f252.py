def buscarTodas(a,b):
    string=[]
    contador=0
    for letra in a:
        enc=letra.find(b)
        if enc==-1:
            next
            contador=contador+1
        else:
            #str(contador)
            string.append(contador)
            contador=contador+1
            
    string2=" ".join(str(x) for x in string)
    return string2
      
#def buscarTodas(a,b):
 #   pass

if __name__ == "__main__":
    pass
           