#Ordenar tres números
a = int(input("ingrese primer digito: "))
b = int(input("ingrese segundo digito: "))
c = int(input("ingrese tercer digito: "))

i= a, b, c
o= a, c, b
s= b, a, c
z= b, c, a
f= c, a, b
k= c, b, a
if (a<=b and b<=c):
  
  print ("",i)
else:
    if(a<=c and c<=b):
      
       print ("",o)
        
    else:
        if(b<=a and a<=c):
          
            print ("",s)
            
        else:
          if(b<=c and c<=a):
            
             print ("",z)
              
          else:
            if(c<=a and a<=b):
              
               print ("",f)
                
            else:
                if(c<=b and b<=a):
                  
                   print ("",k)