def jerigonzo(string):

    largo = len(string)
    i = 0
    palabra = ""
    while i <= largo - 1:

        if string[i]=="a" or string[i]== "e" or string[i]== "i" or string[i]== "o" or string[i]=="u":

            palabra = palabra[0:len(palabra)] + string[i] + "p" + string[i]

        else:
            palabra = palabra + string[i]
        i = i + 1
        
    return palabra