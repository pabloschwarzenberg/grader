# completa el código de la función
def amigos(a,b):
    sumx=0
    sumy=0
    for i in range(1,a):
        if a%i==0:
            sumx+=i
 
    for j in range(1,b):
        if b%j==0:
            sumy+=j
    
    return sumx==b and sumy==a
    if sumx == b and sumy == a:
        return True
    else:
        return False
        
if __name__ == "__main__":
    a= int(input('ingresa un primer numero:'))
    b= int(input('ingresa un segundo numero:'))
