def amigos(a,b):
   num1=a
   num2=b
   numdiv1=[]
   numdiv2=[]
   for i in range(num1-1):
        i=i+1
        if (num1)%i==0:
            numdiv1.append(i)
   for i in range(num2-1):
        i=i+1
        if (num2)%i==0:
            numdiv2.append(i)
   if sum(numdiv1)==num2 and sum(numdiv2)==num1:
        return(True)
   else:
        return(False) 