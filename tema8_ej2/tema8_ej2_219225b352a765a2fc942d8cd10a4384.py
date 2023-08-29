def buscarTodas(a,b):
    string = ""
    i=0
    for letra in a:
        if letra == b:
            if len(string)!= 0:
                string += " "
            string += str(i)
        i+=1
    return string

if __name__ == "__main__":
    pass
           