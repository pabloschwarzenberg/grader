def decodificar(mensaje):
  codigo=mensaje.replace(","," ")
  sub=codigo.split()
  vuelta=len(sub)
  sumatoria=""
  x=0
  for i in range(vuelta):
    if(sub[x]=="01100001"):
        sumatoria=sumatoria+"a"
    elif(sub[x]=="01000010"):
        sumatoria=sumatoria+"b"
    elif(sub[x]=="01000011"):
        sumatoria=sumatoria+"c"
    elif(sub[x]=="01000100"):
        sumatoria=sumatoria+"d"
    elif(sub[x]=="01000101"):
        sumatoria=sumatoria+"e"
    elif(sub[x]=="01000110"):
        sumatoria=sumatoria+"f"
    elif(sub[x]=="01100111"):
        sumatoria=sumatoria+"g"
    elif(sub[x]=="01101000"):
        sumatoria=sumatoria+"h"
    elif(sub[x]=="01001010"):
        sumatoria=sumatoria+"j"
    elif(sub[x]=="01001011"):
        sumatoria=sumatoria+"k" 
    elif(sub[x]=="01101100"):
        sumatoria=sumatoria+"l"
    elif(sub[x]=="01001101"):
        sumatoria=sumatoria+"m"
    elif(sub[x]=="01001110"):
        sumatoria=sumatoria+"n"
    elif(sub[x]=="01101111"):
        sumatoria=sumatoria+"o"
    elif(sub[x]=="01010000"):
        sumatoria=sumatoria+"p"
    elif(sub[x]=="01010001"):
        sumatoria=sumatoria+"q"
    elif(sub[x]=="01010010"):
        sumatoria=sumatoria+"r"
    elif(sub[x]=="01010011"):
        sumatoria=sumatoria+"s"
    elif(sub[x]=="01000100"):
        sumatoria=sumatoria+"t"
    elif(sub[x]=="01010101"):
        sumatoria=sumatoria+"u"
    elif(sub[x]=="01010110"):
        sumatoria=sumatoria+"v"
    elif(sub[x]=="01010111"):
        sumatoria=sumatoria+"w"
    elif(sub[x]=="01011000"):
        sumatoria=sumatoria+"x"
    elif(sub[x]=="01011001"):
        sumatoria=sumatoria+"y"
    elif(sub[x]=="01011010"):
        sumatoria=sumatoria+"z"
    x=x+1
  return(sumatoria) 
         