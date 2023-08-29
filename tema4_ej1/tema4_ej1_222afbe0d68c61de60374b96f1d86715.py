import random
guion='_'
letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']

def ocultar_letras(palabra,cantidad):
    
    
    c=0
    
    palabra=list(palabra)
    
    while c<cantidad:
       p= random.randint(0,(len(palabra)-1))
       if palabra[p] == guion:
           c=c
       else:
           palabra[p] = guion
           c=c+1
        
    
    
    palabra = ''.join(palabra)
    
    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    
    
    
    palabra=list(palabra) 
    palabra_secreta=list(palabra_secreta)
    if letra in palabra_secreta:
        for q in range(0,len(palabra)):
                       if palabra_secreta[q]==letra:
                           palabra[q]=letra
    
    

    palabra = ''.join(palabra)                       
    return palabra

