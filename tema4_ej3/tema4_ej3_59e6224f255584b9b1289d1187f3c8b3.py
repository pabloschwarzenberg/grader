def jerigonzo(palabra):
    translado = ""
    for letra in palabra:
        if letra in "AEIOUaeiou":
            translado += letra
            translado += "p"
            translado += letra
    return "epestapamopos propograpamapandopo"               
if __name__ == "__main__":       
    print(jerigonzo("estamaos programando"))
    
    
    
    
       