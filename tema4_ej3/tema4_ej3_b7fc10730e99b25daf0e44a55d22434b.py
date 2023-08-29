def jerigonzo():
    a = ""
    
    for letra in ():
        
        if letra in "aeiouAEIOU":

            a += "p"
            a+=letra
        a +=letra
    return a

if __name__ == "__main__":
    palabra= input ("ingrese una palabra: ")
    print(jerigonzo(palabra))