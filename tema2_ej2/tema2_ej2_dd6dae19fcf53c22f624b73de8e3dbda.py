# completa el código de la función
def amigos(a,b):
   x= int(2)
   divisorNum=1
   divisorNum2=1
   lisDiv1=[]
   lisDiv2=[]

   if a == b:
     return(False)
   
  
   for i in range (a):
      if a % x ==0:
          divisorNum=(x)
          lisDiv1.append(divisorNum)
          a=a/divisorNum
    
      else:
          x = x+1

   for i in range (b):
       if b % x ==0:
           divisorNum2=(x)
           lisDiv2.append(divisorNum2)
           b=b/divisorNum2
           
       else:
           x = x+1    

   if set(lisDiv1) and set(lisDiv2):
        return(True)
   else:
        return(False)


