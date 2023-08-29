num=int(input("ingresa numero de telefono: "))
h=int(input("igresa hora de la llamada: "))  


digito=(num // (10**5))
ultimos=(num-((num//(10**3))*1000))


if (h>=0) and (h<=7):
      print("la combinacion, ",num ,",",h," es CONTESTAR")

elif  (h<14) and (h>7):
    if (ultimos==909):
      print("la combinacion, ",num ,",",h," es CONTESTAR")
    else:
       print("la combinacion, ",num ,",",h," es NO CONTESTAR")
      

elif  (h>=17) and (19>=h) :
    if (digito==877) :
      print("la combinacion, ",num ,",",h," es NO CONTESTAR")
    else :
        print("la combinacion, ",num ,",",h," es CONTESTAR")
        
elif  (h>19): 
         print("la combinacion, ",num ,",",h," es NO CONTESTAR")
    