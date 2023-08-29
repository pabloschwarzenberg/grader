def jerigonzo(string):
    vocal="aeiouAEIOU"
    traduccion=""
    for letras in string:
        traduccion+=letras
        if letras in vocal:
            traduccion+="p" + letras.lower()
    return traduccion
            
if __name__ == "__main__":
    string=input("Ingresa un texto: ")
    traduccion=jerigonzo(string)
    print("Texto traducido a jerigonzo:",traduccion)
