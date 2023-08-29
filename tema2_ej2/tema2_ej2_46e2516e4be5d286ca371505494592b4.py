def amigos(a, b):
    suma_a=0
    i=1
    while i<a:
        if a%i==0:
            suma_a+=i
            i+=1
        else:
            i+=1
    suma_b=0
    i=1
    while i<b:
        if b%i==0:
            suma_b+=i
            i+=1
        else:
            i+=1
    if suma_a==b and suma_b==a:
        print(str(a) +" y " +str(b) +" son numeros amigos ")
        return True
    else:
        print(str(a) +" y " +str(b) +" NO son numeros amigos ")
        return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    b=int(input("Ingrese b: "))
    print(amigos(a, b))
           