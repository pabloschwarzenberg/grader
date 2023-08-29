# completa el código de la función
def amigos (a,b):
    i=1
    x=0
    y=0
    while i<a and i<b:
        if a%i==0:
            x=x+i
        if b%i==0:
            y=y+i
        i=i+1

    if x==b and y==a:
        return True 
    else:
        return False

       


       



           