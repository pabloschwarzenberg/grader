def rot13(palabra):
    lista=list(palabra)
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    abc2 = ["n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m"]
    encryptar= ""
    for i in lista:
        encryptar += abc2[abc.index(i)]
    return encryptar

           