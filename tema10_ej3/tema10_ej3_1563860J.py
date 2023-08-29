def sopaletras(nombre_archivo,palabras):
    archivo=open(nombre_archivo,"r")
    lista=[]
        for linea in archivo:
            lista.append(str(linea))
    return lista        
            
    archivo.close()
    return [(palabras[0],[0,0],"diagonal")]

if __name__=="__main__":
    pass
    
 import os
 print (os.name)

           