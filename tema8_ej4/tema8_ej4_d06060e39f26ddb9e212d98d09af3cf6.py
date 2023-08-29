def rot13(palabra):
    alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    lista=[]
    for i in palabra:
        if i==" ":
            lista.append(i)
            continue
        else:
            index=(alfabeto.index(i))
        if index>13:
            nuevoIndex=index-13
            letra=alfabeto[nuevoIndex]
            lista.append(letra)
        
        else:
            nuevoIndex= index+13
            letra= alfabeto[nuevoIndex]
            lista.append(letra)
        
    palabra= "".join(lista)
    palabra= palabra.strip()
    return palabra
 

           