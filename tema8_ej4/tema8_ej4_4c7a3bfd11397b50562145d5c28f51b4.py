def rot13(palabra):
    giros=len(palabra)
    x=0
    suma=""
    for i in range(giros):
        palabra[x]
        #1
        if(palabra[x]=="a" or palabra[x]=="n"):
            if(palabra[x]=="n"):
                suma=suma+"a"
            elif(palabra[x]=="a"):
                suma=suma+"n"
        #2
        elif(palabra[x]=="b" or palabra[x]=="o"):
            if(palabra[x]=="b"):
                suma=suma+"o"
            elif(palabra[x]=="o"):
                suma=suma+"b"
        #3
        elif(palabra[x]=="c" or palabra[x]=="p"):
            if(palabra[x]=="c"):
                suma=suma+"p"
            elif(palabra[x]=="p"):
                suma=suma+"c"
        #4
        elif(palabra[x]=="d" or palabra[x]=="q"):
            if(palabra[x]=="d"):
                suma=suma+"p"
            elif(palabra[x]=="p"):
                suma=suma+"d"
        #5
        elif(palabra[x]=="e" or palabra[x]=="r"):
            if(palabra[x]=="e"):
                suma=suma+"r"
            elif(palabra[x]=="r"):
                suma=suma+"e"
        #6
        elif(palabra[x]=="f" or palabra[x]=="s"):
            if(palabra[x]=="f"):
                suma=suma+"s"
            elif(palabra[x]=="s"):
                suma=suma+"f"
        #7
        elif(palabra[x]=="g" or palabra[x]=="t"):
            if(palabra[x]=="g"):
                suma=+"t"
            elif(palabra[x]=="t"):
                suma=suma+"g"
        #8
        elif(palabra[x]=="u" or palabra[x]=="h"):
            if(palabra[x]=="u"):
                suma=suma+"h"
            elif(palabra[x]=="h"):
                suma=suma+"u"
        #9
        elif(palabra[x]=="i" or palabra[x]=="v"):
            if(palabra[x]=="i"):
                suma=suma+"v"
            elif(palabra[x]=="v"):
                suma=suma+"i"
        #10
        elif(palabra[x]=="j" or palabra[x]=="w"):
            if(palabra[x]=="j"):
                suma=suma+"w"
            elif(palabra[x]=="w"):
                suma=suma+"j"
        #11
        elif(palabra[x]=="k" or palabra[x]=="x"):
            if(palabra[x]=="k"):
                suma=suma+"x"
            elif(palabra[x]=="x"):
                suma=suma+"k"
        #12
        elif(palabra[x]=="l" or palabra[x]=="y"):
            if(palabra[x]=="l"):
                suma=suma+"y"
            elif(palabra[x]=="y"):
                sumas=suma+"l"
        #13
        elif(palabra[x]=="m" or palabra[x]=="z"):
            if(palabra[x]=="m"):
                suma=suma+"z"
            elif(palabra[x]=="z"):
                suma=suma+"m"
        x=x+1
    return(suma)

           