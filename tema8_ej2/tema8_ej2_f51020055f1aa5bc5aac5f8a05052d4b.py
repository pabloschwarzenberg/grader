def buscarTodas(a,b):
    salida=""
    indice=0
    espacio =""
    
    for n in range(0,len(a)):
        if a[n].lower()== b.lower():
            salida += espacio + str(indice)
            espacio = " "
        indice +=1      
    
    
    return salida

if __name__ == "__main__":
    pass
           