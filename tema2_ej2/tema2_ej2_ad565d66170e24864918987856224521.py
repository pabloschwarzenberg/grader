# completa el código de la función
def numerosamigos(x,y):
    sumax=0
    sumay=0
    for i in range(1,x):
        if x%i==0:
            suma_x+=i
 
    for k in range(1,y):
        if y%k==0:
            suma_y+=k
 
    return suma_x==y and suma_y==x

no=int(input("Introduzca el nº 1: "))
na=int(input("Introduzca el nº 2: "))
 
if numerosamigos(no,na):
    print ("Son amigos :)")
else:
    print ("No son amigos :(")