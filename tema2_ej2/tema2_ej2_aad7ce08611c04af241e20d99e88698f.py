# completa el código de la función
def amigos(a,b):
    divisores_a= 1
    divisores_b = 1
    sum_div_a=0
    sum_div_b = 0
    while divisores_a<a:
        if a%divisores_a == 0:
            sum_div_a=sum_div_a+ divisores_a
        divisores_a+=1
    while divisores_b<b:
        if b%divisores_b == 0:
            sum_div_b=sum_div_b + divisores_b
        divisores_b+=1
    if sum_div_a==b and sum_div_b==a:
        return True
    else:
        return False

print(amigos(220, 284))
      
   
    
     
    
           