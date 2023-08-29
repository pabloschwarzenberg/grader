# completa el código de la función
def divisores_a(a):
    for i in range (2,a-1):
        if a%i !=0:
            break
        else:
            c=i           
    divisores_a = c +c              
def divisores_b (b):
    for i in range (2,b-1):
        if b%i !=0:
            break
        else:
            d=i 
    divisores_b = d+ i       
def amigos(a,b,divisores_a , divisores_b):
    if (divisores_a== b):
        return True
    elif (divisores_b ==a):
        return True
    else:
        return False
      
           