def decodificar(mensaje):
    L = mensaje.split(",")    
    string_2=""
    for string_1 in L:
            if string_1=="01100001":
                string_2=string_2+"a"
            elif string_1=="01100010":
                string_2=string_2+"b"
            elif string_1=="01100011":
                string_2=string_2+"c"
            elif string_1=="01100100":
                string_2=string_2+"d"
            elif string_1=="01100101":
                string_2=string_2+"e"
            elif string_1=="01100110":
                string_2=string_2+"f"
            elif string_1=="01100111":
                string_2=string_2+"g"
            elif string_1=="01101000":
                string_2=string_2+"h"
            elif string_1=="01101001":
                string_2=string_2+"i"
            elif string_1=="0110 1010":
                string_2=string_2+"j"
            elif string_1=="01101011":
                string_2=string_2+"k"
            elif string_1=="01101100":
                string_2=string_2+"l"
            elif string_1=="01101101":
                string_2=string_2+"m"
            elif string_1=="01101110":
                string_2=string_2+"n"
            elif string_1=="01101111":
                string_2=string_2+"o"
            elif string_1=="01110000":
                string_2=string_2+"p"
            elif string_1=="01110001":
                string_2=string_2+"q"
            elif string_1=="01110010":
                string_2=string_2+"r"
            elif string_1=="01110011":
                string_2=string_2+"s"
            elif string_1=="01110100":
                string_2=string_2+"t"
            elif string_1=="01110101":
                string_2=string_2+"u"
            elif string_1=="01110110":
                string_2=string_2+"v"
            elif string_1=="01110111":
                string_2=string_2+"w"
            elif string_1=="01111000":
                string_2=string_2+"x"
            elif string_1=="01111001":
                string_2=string_2+"y"
            elif string_1=="01111010":
                string_2=string_2+"z"
    
    return string_2
