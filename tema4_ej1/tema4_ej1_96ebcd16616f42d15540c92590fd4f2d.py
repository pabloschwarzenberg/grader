from random import randint
def ocultar_letras(palabra,cantidad):
    palabra = list(palabra)
    a = []
    palabra_str = ""
    
    for i in range(cantidad):
        a.append(randint(0, len(palabra)))
        
    for d in range(len(a)):
        palabra[a[d] - 1]  = "_"
    for letra in range(len(palabra)):
        palabra_str = palabra_str + palabra[letra]      
        
    return palabra_str

def revisar_letra(palabra_secreta,palabra,letra):
    if len(palabra_secreta) == len(letra):
        return palabra_secreta
    else: 
        pass
        
    palabra_secreta, palabra = list(palabra_secreta), list(palabra)
    for letras in range(len(palabra_secreta)): 
        if palabra_secreta[letras] == letra:
            palabra[letras] = letra
        else:
            pass
    palabra_str = ""
    for i in range(len(palabra)):
        palabra_str = palabra_str + palabra[i] 
    
    return palabra_str
    

if __name__ == "__main__":
    pass
         