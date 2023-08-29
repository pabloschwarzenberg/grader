def jerigonzo (palabra):
    i=0
    palabra_1=list(palabra)
    largo=len(palabra_1)
    for i in range(0,largo):
       if palabra_1[i]=="a":
          palabra_1[i]="apa"
          palabra="".join(palabra_1)
   
       elif palabra_1[i]=="e":
            palabra_1[i]="epe"
            palabra="".join(palabra_1)
        
       elif palabra_1[i]=="i":
            palabra_1[i]="ipi"
            palabra="".join(palabra_1)
       
       elif palabra_1[i]=="o":
            palabra_1[i]="opo"
            palabra="".join(palabra_1)
   
       elif palabra_1[i]=="u":
            palabra_1[i]="upu"
            palabra="".join(palabra_1)
    return (palabra)
if __name__ == "__main__":
  palabra=input("Ingrese una palabra ")
  print(jerigonzo(palabra))

  