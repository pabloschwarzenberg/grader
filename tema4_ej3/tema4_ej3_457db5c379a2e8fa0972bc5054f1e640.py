def jerigonzo(string):
    texto=''
    for i in range(len(string)):
        if string[i]=='a' or string[i]=='e' or string[i]=='i' or string[i]=='o' or string[i]=='u':
            texto+=string[i]+'p'+string[i]
        else:
            texto+=string[i]
    return texto
         