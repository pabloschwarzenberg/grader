def rot13(palabra):
    i=0
    STR=""
    while i<len(palabra):
            AN=palabra[i]
        
            if AN=="a":
                STR=STR+("n")
            if AN=="b":
                STR=STR+("o")
            if AN=="c":
                STR=STR+"p"
            if AN=="d":
                STR=STR+"q"

            if AN=="e":
                STR=STR+"r"

            if AN=="f":
                STR=STR+"s"
            
            if AN=="g":
                STR=STR+"t"
            if AN=="h":
                STR=STR+"u"
               
            if AN=="i":
                STR=STR+"v"
                
            if AN=="j":
                STR=STR+"w"
                
            if AN=="k":
                STR=STR+"x"
                
            if AN=="l":
                STR=STR+"y"
                
            if AN=="m":
                STR=STR+"z"
            
            if AN=="z":
                STR=STR+"m"
            if AN=="y":
                STR=STR+"l"
            if AN=="x":
                STR=STR+"k"
            if AN=="w":
                STR=STR+"j"
            if AN=="v":
                STR=STR+"i"
            if AN=="u":
                STR=STR+"h"
            if AN=="t":
                STR=STR+"g"
            if AN=="s":
                STR=STR+"f"
            if AN=="r":
                STR=STR+"e"
            if AN=="q":
                STR=STR+"d"
            if AN=="p":
                STR=STR+"c"
            if AN=="o":
                STR=STR+"b"
            if AN=="n":
                STR=STR+"a"
            
            i=i+1
        
    return STR