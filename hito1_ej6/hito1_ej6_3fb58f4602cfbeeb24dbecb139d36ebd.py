#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())

condition_1= (a>=b) and (a>=c) and (b>=c) 
if (condition_1):
   print(c,"," ,b ,"," ,a)

condition_2= (a<=c) and (a<=b) and (b<=c)
if (condition_2):
   print(a,",", b ,"," ,c)
 
condition_3= (b>=c) and (b>=a) and (a>=c)
if (condition_3):
   print(c, "," , a ,"," , b)
  
condition_4 = (b<=c) and (a<=c) and (b<=a)
if (condition_4):
   print(b, "," , a , "," , c)
   
condition_5 = (a<=b) and (c<=b) and (c>=a) 

if (condition_5):
   print(a , "," , c , "," , b)
 
condition_6 = (c<=a) and (b<=a) and (b<=c)
if (condition_6):
   print(b ,",", c,  "," , a)