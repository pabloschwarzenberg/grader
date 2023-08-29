def jerigonzo(palabra):
    
    
    cambio = []
    for letra in palabra:
        
        if letra in "aeiou":
            
            
            letra = letra + "p"+ letra
        cambio.append(letra)
    cambio = "".join(cambio)
    return cambio
