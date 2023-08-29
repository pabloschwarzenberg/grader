def jerigonzo(string):  
    k=0
    lista=[]
    for caracter in string:      
        if caracter != 'a' or caracter != 'e' or caracter != 'i' or caracter != 'o' or caracter != 'u':
            lista.append(caracter)
        if caracter == 'a' or caracter == 'e' or caracter == 'i' or caracter == 'o' or caracter == 'u':         
            x = str('p')+str(caracter)
            lista.append(x)
    lista = "".join(lista)
    string = lista
    return string