def jerigonzo(string):
    lista =[]
    for i in string:
        
        
        if i != "o":
            lista.append(i)
        if i == "o":
            lista.append(i + "p" + i)

        if i == "a":
            lista.append("p" + i)
        
        if i == "e":
            lista.append("p" + i)

        if i == "i":
            lista.append("p" + i)
           
        if i == "u":
            lista.append("p" + i)
        
    return ((''.join(lista)))
         