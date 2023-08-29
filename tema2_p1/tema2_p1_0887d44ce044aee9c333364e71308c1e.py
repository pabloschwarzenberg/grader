# por favor escribe aquí tu función
def es_primo(num):
    if (num<=1):
        return False
 
    for i in range(2, (num)+1):
        if(num%i==0 and i!=num):
            return False
    return True
 
while True:
    try:
        num = int(input("inserta un numero o ingresa (0) para salir "))
        if es_primo(num):
            print ("True %s" % num)
        else:
            print ("False %s" % num)
    except:
        print ("El numero tiene que ser entero")
    break
