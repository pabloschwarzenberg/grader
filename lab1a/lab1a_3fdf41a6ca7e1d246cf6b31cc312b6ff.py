#Elecciones
totalcomuna1=int(input("ingrese total votos comuna 1"))
totalcomuna2=int(input("ingrese total votos comuna 2"))
totalcomuna3=int(input("ingrese total votos comuna 3"))
votoscomuna1=int(input("votos isabel comuna 1"))
votoscomuna2=int(input("votos isabel comuna 2"))
votoscomuna3=int(input("votos isabel comuna 3"))




totalvotos=totalcomuna1 +totalcomuna2 +totalcomuna3
votosisabel=votoscomuna1 + votoscomuna2 + votoscomuna3

vtp=(totalvotos*40)/100

if vtp<=votosisabel:
    print("senadora electa")
    
else:
    

    porcentajevotos=(totalvotos*70)/100
    aux1=votoscomuna1 +votoscomuna2
    if porcentajevotos<=aux1:
         print("senadora electa")
  
    
    else :
          porcentajevotos=(totalvotos*70)/100
          aux2=votoscomuna1 +votoscomuna3
          if porcentajevotos<=aux2:
                print("senadora electa")
          else:    
               porcentajevotos=(totalvotos*70)/100
               aux3=votoscomuna2 +votoscomuna3
               if porcentajevotos<=aux3:
                   print("senadora electa")
               else:
    
                 
                 
                    porcentajevotos=(totalvotos*80)/100
                    if porcentajevotos<=votoscomuna1 or porcentajevotos<=votoscomuna2 or porcentajevotos<=votoscomuna3:
                        print("senadora electa")
                    else:
                        print("candidata perdedora")

                 
