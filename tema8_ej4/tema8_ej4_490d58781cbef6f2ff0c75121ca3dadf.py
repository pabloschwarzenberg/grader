def rot13(palabra):
    string=list(palabra)
    abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    cambio=["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
    encriptado=""
    for i in string:
      encriptado+=cambio[abecedario.index(i)]
    return encriptado