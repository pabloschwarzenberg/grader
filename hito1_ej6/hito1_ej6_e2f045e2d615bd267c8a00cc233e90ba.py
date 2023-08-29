a=int(input('ingresa un numero:'))
b=int(input('ingresa un numero:'))
c=int(input('ingresa un numero:'))
	
	
if a>c and c>b:
  print(str(b)+','+str(c)+','+str(a))
  
elif a>b and b>c:
  print(str(c)+','+str(b)+','+str(a))
  
elif b>c and a<c:
  print(str(a)+','+str(c)+','+str(b))
  
elif b>a and c<a:
  print(str(c)+','+str(a)+','+str(b))
	
elif c>b and a<b:
  print(str(a)+','+str(b)+','+str(c))
    
elif c>a and a>b:
  print(str(b)+','+str(a)+','+str(c))
  
elif a>b or a>c:
   print(str(b)+','+str(c)+','+str(a))
   
elif b>a or b>c:
   print(str(a)+','+str(c)+','+str(b))
   
elif c>a or c>b:
   print(str(b)+','+str(b)+','+str(c))
  