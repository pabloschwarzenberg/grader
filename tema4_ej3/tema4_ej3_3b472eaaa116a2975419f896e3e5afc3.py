def jerigonzo(string):
    s=string.split()
    jer=""
    for letra in string:
        jer=jer+letra
        if letra in "AEIOUaeoiu":
            jer+="p"+letra
            
    return jer

if __name__ == "__main__":
    print(jerigonzo("hola soy maximiliano rojel"))
    pass
         
         
         