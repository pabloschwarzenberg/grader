Ni=int(input("ingrese numero de inicio."))
Nf=int(input("ingrese numero de fin."))
while  Ni<=Nf:
    Ba=Ni%2
    Bb=Ni%7
    if Ba==0 or Bb==0:
        print (Ni)
    Ni=Ni+1
    
    