def buscarTodas(a,b):
    cuenta=""
    if b in a:
        for i in range(len(a)):
            if a[i]==b:
                cuenta+=str(i)
                cuenta+=" "
        return(cuenta.strip())
       