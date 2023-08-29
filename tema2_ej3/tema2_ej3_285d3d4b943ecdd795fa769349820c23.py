def numero_perfecto(a):
    np = [ ]
    for n in range (1,a+1):
        if a%n == 0:
            np.append(n)
    sumanp = sum(np)
    rsuma = sumanp - a
    
    if rsuma == a:
        return True
    elif rsuma != a:
        return False
    
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           