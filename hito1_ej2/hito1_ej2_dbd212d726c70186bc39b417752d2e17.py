#Si la llamada ocurre entre 00:00 y 07:00, la contestas ya que podría ser una emergencia.
#Si ocurre antes de las 14:00 no la contestas, excepto si el número termina en 909.
#Durante la tarde, solamente contestas entre 17:00 y 19:00, exceptuando un número que comienza por 877.
#Después de las 19:00, no contestas el celular.
a = input("ingrese número telefónico:")
h = input("ingrese hora de llamada:")
n = ((a[len(a)-3:len(a)]) != 909 )

#algoritmo 
if  (0 <= int(h) <= 7):
    print("Contestar")

if  (8 <= int(h) <= 14):
    print("NO CONTESTAR")
    
elif (8 <= int(h) <= 14) and (a[len(a)-3:len(a)]):
    print("CONTESTAR")
              
     
#elif 8 <= int(h) <= 14:
   #print (a[len(a)-3:len(a)]) != (a[len(a)-3:len(a)]
    #print("NO CONTESTAR")
    
if (15 <= int(h) <= 16):
    print("NO CONTESTAR")


if (17 <= int(h) <= 19):
    print("NO CONTESTAR")
   

elif (17 <= int(h) <= 19):
    print("CONTESTAR")
     
  
if (20 <= int(h) <= 23):
    print("NO CONTESTAR")