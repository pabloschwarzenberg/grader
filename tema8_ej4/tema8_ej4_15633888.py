def rot13(palabra):
    alfabeto=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    np=""
    for i in range(len(palabra)):

        if palabra[i]!=" ":

            ub_i=alfabeto.index(palabra[i])

            np+=alfabeto[(ub_i+13)%52]
        else:
            np+=" "
    return np.lower()
    

if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)
           