#Contestador de celular
num = int(input())
hora = int(input())

if 0<hora<7:
   print("CONTESTAR")
else:
    if 7<hora<14 and (num%1000)==909:
          print("CONTESTAR")
    else:
        if 7<hora<14 and not(num%1000==909):
           print("NO CONTESTAR")
        else:
            if 17<hora<19 and not(num//100000==877):
               print("CONTESTAR")
            else:
                if 17<hora<19 and num//100000==877:
                   print("NO CONTESTAR")
                else:
                    if hora>19:
                       print("NO CONTESTAR")
        

 