#Descomponer un número
x=input()
if len(x)==4:
    mil=int(x[0])
    cien=int(x[1])
    dies=int(x[2])
    uno=int(x[3])
    print(str(mil)+"M"+"+"+str(cien)+"C"+"+"+str(dies)+"D"+"+"+str(uno)+"U")
if len(x)==3:
    cien=int(x[0])
    dies=int(x[1])
    uno=int(x[2])
    print(str(cien)+"C"+"+"+str(dies)+"D"+"+"+str(uno)+"U")
if len(x)==2:
     dies=int(x[0])
     uno=int(x[1])
     print(str(dies)+"D"+"+"+str(uno)+"U")
if len(x)==1:
    uno=int(x[0])
    print(str(uno)+"U")
    
          
          
