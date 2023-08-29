    substring="GTAGTC"
    resto="GATT"
    encontre="si"
    #largo_sub=2
    #print ("a:",a,"b:",b)
    #seguir=input("Precione c, para continuar con el juego:")
    j=0
    i=0
    
    while i<=(len(palabra)) or i<=(len(palabra2)):
        #largo_sub=i+largo_sub
        #substring=palabra[i:largo_sub+i]
        #print(i)
        #print(len(palabra))
        #print(len(palabra2))
        #print(substring)
        #seguir=input("Precione c, para continuar con el juego:")
        j=0
        while j <=(len(palabra2)):
            if palabra2[i:1] != palabra[j:1]:
               palabra_salida3= palabra_salida3 + palabra[i:1]
               palabra_salida4= palabra_salida4 + "_"
            else:
               palabra_salida4=palabra_salida4 + palabra[i:1]
               palabra_salida3=palabra_salida3 + palabra[j:1]
            if encontre=="si":
                print ("palabra2:",palabra2)
                palabra_salida=palabra[0:5] + "__" + palabra[5:]
                palabra_salida2="___" + palabra2[0:8] +"*"
                palabra_salida2= palabra_salida2 + substring + "__"
                palabra_salida2= palabra_salida2 + resto
                encontre="no"
            j=j+1    
        i=i+1

    print(palabra_salida,palabra_salida2
    #return palabra_salida, palabra_salida2    