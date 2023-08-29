# completa el código de la función
def amigos(a,b):
    d=0
    f=0
    for i in range(a):
        if (a%(i+1))==0:
            d=d+i+1
            print(str(d))
            continue
        else:
            continue
    print("cambio!!")        
    for j in range(b):
        if (b%(j+1))==0:
            f=f+j+1
            print(str(f))
            continue
        else:
            continue
    if a==b:
        return 1==2
    else:
        return (f==d)
        
            
if __name__ == "__main__":

    print("¿Quieres saber si dos números son amigos?")
    a=int(input("ingresa el primer número"))
    b=int(input("ingresa el otro numero"))
    print(str(amigos(a,b)))
    
