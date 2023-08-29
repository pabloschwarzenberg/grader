def rot13(palabra):
    palabra=palabra.upper()
    palabra_1=list(palabra)
    largo=len(palabra_1)
    for i in range(0,largo):
        if palabra_1[i]=="A":
           palabra_1[i]="N"
           palabra="".join(palabra_1)
           
        elif palabra_1[i]=="B":
             palabra_1[i]="O"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="C":
             palabra_1[i]="P"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="D":
             palabra_1[i]="Q"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="E":
             palabra_1[i]="R"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="F":
             palabra_1[i]="S"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="G":
             palabra_1[i]="T"
             mayuscula="".join(palabra_1)
           
        elif palabra_1[i]=="H":
             palabra_1[i]="U"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="I":
             palabra_1[i]="V"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="J":
             palabra_1[i]="W"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="K":
             palabra_1[i]="X"
             palabra="".join(palabra_1)

        elif palabra_1[i]=="L":
             palabra_1[i]="Y"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="M":
             palabra_1[i]="Z"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="N":
             palabra_1[i]="A"
             palabra="".join(palabra_1)
 
        elif palabra_1[i]=="O":
             palabra_1[i]="B"
             palabra="".join(palabra_1)

           
        elif palabra_1[i]=="P":
             palabra_1[i]="C"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="Q":
             palabra_1[i]="D"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="R":
             palabra_1[i]="E"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="S":
             palabra_1[i]="F"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="T":
             palabra_1[i]="G"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="U":
             palabra_1[i]="H"
             palabra="".join(palabra_1)
           
           
        elif palabra_1[i]=="V":
             palabra_1[i]="I"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="W":
             palabra_1[i]="J"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="X":
             palabra_1[i]="K"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="Y":
             palabra_1[i]="L"
             palabra="".join(palabra_1)
           
        elif palabra_1[i]=="Z":
             palabra_1[i]="M"
             palabra="".join(palabra_1)
           
      
           
       
    return palabra.lower()   

if __name__=="__main__":

  
  n1=input("Ingresa la palabra que quieras encriptar: ")
  resultado=rot13(palabra)
  print("El resultado es: ",resultado)
    