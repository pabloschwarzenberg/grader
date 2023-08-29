#Contestador de celular
n=str(input( "ingrese numero telefonico: " ))

hr=int(input( "ingrese hora de la llamada: " ))

         
if hr > 0 and hr < 7:
    print("CONTESTAR")
if hr > 19 and hr <=23:
    print("NO CONTESTAR")
    


else:
    
    if hr > 7 and hr < 14 and str(n[-3])=="9" and str(n[-2])=="0" and str(n[-1])=="9":
        print("CONTESTAR")
        
    if hr > 7 and hr < 14 and str(n[-3])!="9" and str(n[-2])!="0" and str(n[-1])!="9":
        print("NO CONTESTAR")
        
   
    if hr > 17 and hr<=19 and str(n[0:1])=="8" and str(n[1:2])== "7" and str(n[2:3])== "7":
        print("NO CONTESTAR")
        
    if hr > 17 and hr <=19 and str(n[0:1])!="8" and str(n[1:2])!= "7" and str(n[2:3])!= "7":
        print("CONTESTAR")
        
         