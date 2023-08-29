def amigos(a,b):

    K=1
    
    F=1
    
    L=0
    
    Q=0
    
    while K<a:
    
        if a%K==0:
        
            L+=K
            
        K+=1
        
    while F<b:
    
        if b%F==0:
        
            Q+=F
            
        F += 1
        
    if L==b and Q==a:
    
        return True
        
    else:
    
        return False

try:

   a = int(input("introduzca un numero :D :"))
   
   b = int(input("introduzca un numero :D :"))
 
   if amigos(a,b):
   
    print("True")

   else:
   
    print("False")

except EOFError as e:

    print(e)
