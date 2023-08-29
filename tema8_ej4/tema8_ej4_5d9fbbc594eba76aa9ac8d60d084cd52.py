def rot13(palabra):
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
           "q","r","s","t","u","v","w","x","y","z"]
    abcrot = ["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b",
              "c","d","e","f","g","h","i","j","k","l","m"]
    palabraF = ""
    palabra = palabra.lower()
    for a in range(len(palabra)):
        for b in range(len(abc)):
            if palabra[a] == abc[b]:
                palabraF+=abcrot[b]
        
    return palabraF

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           