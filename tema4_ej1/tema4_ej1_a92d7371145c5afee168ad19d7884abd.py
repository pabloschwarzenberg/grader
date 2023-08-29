import random

def ocultar_letras(palabra,cantidad):
    palabra_lista=list(palabra)

    i=0
    while i <= cantidad:
        n_random=random.randint(0,len(palabra))
        if palabra_lista[n_random] != "_":
          palabra_lista[n_random]="_"
        i+=1
        palabra_final="".join(palabra_lista)
    
    return palabra_final

def revisar_letra(palabra_secreta,palabra,letra):
    
    palabra_secreta_lista=list(palabra_secreta)
    palabra_lista=list(palabra)
    posicion=0
    contador=0
    for i in palabra_secreta_lista:
        if i == letra:
            palabra_lista[posicion]=letra
            contador += 1
        
        posicion += 1
            
        
    palabra="".join(palabra_lista)
    return palabra




"""
if __name__ == "__main__":
    

   
    lista=["lepidoptero1","lepidoptero2","lepidoptero3"]
    palabra_secreta=lista[random.randint(0,len(lista))]

    
    intentos =0
    while intentos <=7:
        strg=str(input("ingresaletra"))
        print(revisar_letra("lepidoptero", revisar_letra(palabra_secreta,palabra,letra), strg)[0])
        intentos +=1

            
   """         




