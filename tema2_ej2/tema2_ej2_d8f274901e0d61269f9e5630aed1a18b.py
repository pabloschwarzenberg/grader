# completa el código de la función
def amigos(a,b):
    xd = 1
    yd = 1
    xl = 0
    yl = 0
    L=[]
    Z=""

#Bucle while (Divisiones y sumatoria) return true
    while yd < b:

        if b%yd == 0:
            yl+= yd
        yd+= 1

    while xd < a:

        if a%xd == 0:
            xl+= xd
        xd+= 1
        
    if xl == b and yl == a:
        return True
    
#else return false
    else:
        return False
    
#Try for another way again :((((((((
try:
    x = int(input("Ingrese un numero: "))
    y = int(input("Ingrese otro numero: "))
    print(amigos(x,y))
          
except:
    pass