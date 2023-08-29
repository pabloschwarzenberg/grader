from random import randint
opciones=("python","universidad","hito","coronavirus","cuarentena","covid","ayuda")
secreto=opciones[randint(0,6)]

def ocultar_letras(palabra,cantidad):
    
    oculta=[]
    cambio=[]
    while len(cambio)!=cantidad:
        num=randint(0,len(palabra)-1)
        
        if num not in cambio:
            cambio.append(num)
            
    for i in range(0,len(palabra)):
        oculta.append(palabra[i])
        
    for i in range(0,len(cambio)):
        oculta[cambio[i]]="_"
        
    palabra="".join(oculta)
    return (palabra)

def revisar_letra(palabra_secreta, palabra, letra):
    
    lista_secreta=[]
    lista_palabra=[]
    largo=len(palabra_secreta)
    
    for i in range(0,largo):
        lista_secreta.append(palabra_secreta[i])
        lista_palabra.append(palabra[i])
    
    if letra in lista_secreta:
        
        for i in range(0,largo):
            
            if lista_secreta[i]==letra:
                
                lista_palabra[i]=letra
        palabra="".join(lista_palabra)
    return palabra