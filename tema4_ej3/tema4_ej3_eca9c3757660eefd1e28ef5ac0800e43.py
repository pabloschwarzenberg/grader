def jerigonzo(string):
    convertir=""
    for letra in string:
        if letra in "AEIOUaeiou":
            convertir+=letra
            convertir+="p"
        convertir+=letra    
    return(convertir)

if __name__ == "__main__":
   palabra=input("Ingrese una palabra")
   traducida= jerigonzo(palabra)
   print("La palabra en jerigonzo es:",traducida)
         