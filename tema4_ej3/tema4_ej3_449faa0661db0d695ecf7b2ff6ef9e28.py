def jerigonzo(string):
    nueva=""
    for i in range(len(string)):
        if string[i] in "aeiou":
            nueva+=(string[i]+"p"+string[i])
        else:
            nueva+=string[i]
    return(nueva)        