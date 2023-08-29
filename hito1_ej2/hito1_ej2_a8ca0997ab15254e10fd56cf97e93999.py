#Contestador de celular
seguir=True

while seguir:
 NT=int(input(""))
 NH=int(input(""))
 T=NT%1000
 L=len(str(NT))
 La=str(NT) 
 if L==8:    
    
    if NH>=24:
         print("Seleccione hora correcta")
     

    elif NH<=7:
         print("CONTESTAR")

         seguir=False

    elif NH<=14 and T==909:
         print("CONTESTAR")
         seguir=False

    elif NH==19 or NH==18 or NH==17 and La[0]==8 and La[1]==7 and La[2]==7:       
         print("NO CONTESTAR")
         seguir=False

    elif NH==19 or NH==18 or NH==17:
         print("CONTESTAR")
         seguir=False

    elif NH>19:
         print("NO CONTESTAR")

         seguir=False 

 else:
     print("POR FAVOR DIGITE 8 NUMEROS") 