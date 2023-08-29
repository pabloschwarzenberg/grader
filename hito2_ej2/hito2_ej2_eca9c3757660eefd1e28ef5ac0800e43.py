def validarsecuencias(string):
    palabra=string.upper()
    resultado=0
    for letra in palabra:
        
        if letra in "A,C,T,G":
                 resultado+=1
            
        if letra not in "A,C,T,G":
                 resultado+=0
    if resultado==len(palabra):
        respuesta="secuencia correcta"
    if resultado!=len(palabra):
        respuesta="secuencia incorrecta"
    print(respuesta)    
            
strings=input("")
secuencia=validarsecuencias(strings)      