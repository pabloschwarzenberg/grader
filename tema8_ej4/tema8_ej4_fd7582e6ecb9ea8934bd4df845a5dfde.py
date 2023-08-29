def rot13(palabra):
    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    palabra.lower
    print(len(abc))

    
    
    cifrado=""
    for i in palabra:
        if i in abc:
            if abc.index(i)<13:
                cifrado+=abc[abc.index(i)+13]
            else:
                cifrado+=abc[abc.index(i)-13]
    return cifrado
                