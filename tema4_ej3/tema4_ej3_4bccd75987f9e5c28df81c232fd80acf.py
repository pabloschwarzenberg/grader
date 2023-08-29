def jerinzoso(string):
    string=""
    for f in a:
        string+=f
        if f=="a" or f=="e" or f=="i" or f=="o" or f=="u" or f=="A" or f=="E" or f=="I" or f=="O" or f=="U":
            string = string + "p" + f.lower()
    return(string)
         