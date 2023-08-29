#pal = input("Ingrese la palabra: ")

#print("llego")
def jerigonzo(string):
    
    lista = ""
    #print("llego0")
    
    for letra in string:
        #print("llego1")
        if letra in "AEIOUaeiou":
            #print("llego2")
            lista += letra
            lista += "p"
            
        lista += letra
    
    print(lista)
    
    return lista

    

if __name__ == "__main__":
    
    
    jerigonzo(string)
    #print(jerigonzo(pal))
    #pass
    