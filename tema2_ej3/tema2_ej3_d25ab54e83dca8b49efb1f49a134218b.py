def numero_perfecto (x):
    listaa = [] 

    for i in range( 1,x+1 ): 
        if x % i == 0: 
            listaa.append(i)
    listaa.remove(x)
    if x==sum(listaa):
        return True
    else:
        return False
if __name__ == "__main__":
    x =int(input("Ingrese a: "))
    print(numero_perfecto(n))