def numero_perfecto(num):
 sum=0
 for i in range (1,num):
     if (num % i==0):
         sum+=i
         
 if num==sum:
    return True
 else:
    return False 
