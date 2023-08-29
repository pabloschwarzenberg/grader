 if __name__ == "__main__":
 
 def jerigonza(original):
    traducida = ""
    for letra in original:
        traducida += letra
        if letra.lower() in "aeiou":
            traducida += "p" + letra
    return traducida
    
