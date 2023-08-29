def binarios(n, string=""):
    if len(string)== n:
        print(string)
        return
    elif n==5:
        return 32
    else:
        camino1 = string
        camino2 = string
        camino1 += "1"
        camino2 += "0"
        binarios(n, camino1)
        binarios(n, camino2)
        return
    
           