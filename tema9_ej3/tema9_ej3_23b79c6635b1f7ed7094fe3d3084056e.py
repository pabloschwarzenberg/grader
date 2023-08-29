def decodificar(mensaje):
    mensajefinal = ""
    mensajedividido = mensaje.replace("," , " ")
    mensajedividido = mensajedividido.split()
    letrasmins = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    letrasmayus = []
    binariomin = []
    binariomayus = []
    
    for i in range (len(letrasmins)):
        letrasmayus.append(letrasmins[i].upper())
    
    for i in range(len(letrasmins)):
        binariomin.append(ConverToBin(letrasmins[i]))
        binariomayus.append(ConverToBin(letrasmayus[i]))
        
    for i in range(len(mensajedividido)):
        if (mensajedividido[i] in binariomin):
            for j in range (len(binariomin)):
                if (mensajedividido[i] == binariomin[j]):
                    mensajefinal += letrasmins[j]
                    break
                
        if (mensajedividido[i] in binariomayus):
            for j in range (len(binariomayus)):
                if (mensajedividido[i] == binariomayus[j]):
                    mensajefinal += letrasmayus[j]
                    break
    return (mensajefinal)

def ConverToBin(letra):
    letrabin = bin(ord(letra))
    letrabin = letrabin.replace("b", "")
    return (letrabin)   

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         