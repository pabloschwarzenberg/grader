def decodificar(mensaje):
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
def decodificar(mensaje):
    codigo=mensaje.replace(","," ")
    sub=codigo.split()
    giros=len(sub)
    suma=""
    x=0
    for i in range(giros):
        #a
        if(sub[x]=="01100001"):
            suma=suma+"a"
        #b
        elif(sub[x]=="01000010"):
            suma=suma+"b"
        #c
        elif(sub[x]=="01000011"):
            suma=suma+"c"
        #d
        elif(sub[x]=="01000100"):
            suma=suma+"d"
        #e
        elif(sub[x]=="01000101"):
            suma=suma+"e"
        #f
        elif(sub[x]=="01000110"):
            suma=suma+"f"
        #g
        elif(sub[x]=="g"):
            suma=suma+"g"
        #h
        elif(sub[x]=="01101000"):
            suma=suma+"h"
        #j
        elif(sub[x]=="01001010"):
            suma=suma+"j"
        #k
        elif(sub[x]=="01001011"):
            suma=suma+"k" 
        #l
        elif(sub[x]=="01101100"):
            suma=suma+"l"
        #m
        elif(sub[x]=="01001101"):
            suma=suma+"m"
        #n
        elif(sub[x]=="01001110"):
            suma=suma+"n"
        #o
        elif(sub[x]=="01101111"):
            suma=suma+"o"
        #p
        elif(sub[x]=="01010000"):
            suma=suma+"p"
        #q
        elif(sub[x]=="01010001"):
            suma=suma+"q"
        #r
        elif(sub[x]=="01010010"):
            suma=suma+"r"
        #s
        elif(sub[x]=="01010011"):
            suma=suma+"s"
        #t
        elif(sub[x]=="01000100"):
            suma=suma+"t"
        #u
        elif(sub[x]=="01010101"):
            suma=suma+"u"
        #v
        elif(sub[x]=="01010110"):
            suma=suma+"v"
        #w
        elif(sub[x]=="01010111"):
            suma=suma+"w"
        #x
        elif(sub[x]=="01011000"):
            suma=suma+"x"
        #y
        elif(sub[x]=="01011001"):
            suma=suma+"y"
        #z
        elif(sub[x]=="01011010"):
            suma=suma+"z"
        x=x+1
    return(suma) 
         
    