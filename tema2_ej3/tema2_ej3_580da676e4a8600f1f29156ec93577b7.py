def numero_perfecto(x):
    
    div=[]
    for y in range(1, x):
        divi = x % y
        if(divi == 0):
            div.append(y)
            
    su = sum(div)
    if (su == x):
        return True
    else:
        return False

if __name__ =="__main__":
    x = int(input("Ingrese a: "))
    print(numero_perfecto(x))