#Contestador de celular
print("numero de telefono")
N=(input()) 

print("hora de llamada")
H=int(input())

if(H<=7):
        print("CONTESTAR")
else:
        if(H<14):
            a = N[5]
            b = N[6]
            c = N[7]
            if(a=="9" and b=="0" and c=="9"):
                print("CONTESTAR")
            else:
                print("NO CONTESTAR")
            
            

        else:
                if(H<17):
                    
                    print("NO CONTESTAR")
                    
        
                else:
                      if(H<=19):
                            d = N[0]
                            f = N[1]
                            e = N[2]
                            if(d=="8" and f=="7" and e=="7"):
                             print("NO CONTESTAR")   
                            else:
                             print("CONTESTAR")
                        
                      else:
                            if(H<=23):

                               print("NO CONTESTAR")
 