#Contestador de celular
telefono=int(input())
hora=int(input())
x=telefono%1000
y=telefono//100000



if 0<=hora<=7 :
 print("CONTESTAR")
elif x==909 and hora<14 :
   print("CONTESTAR")
elif x!=909 and hora<14 :
    print("NO CONTESTAR")
elif y==877 and 17<hora<19 :
      print("NO CONTESTAR")
elif y!=877 and 17<hora<19 :
        print("CONTESTAR")
elif hora>19 :
          print("NO CONTESTAR")
else:
    print('NO CONTESTAR')
 
    
    
  