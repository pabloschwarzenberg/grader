def amigos(num): 
    suma = 0 
 
    for i in range(1,num): 
        if num % i == 0: 
            suma += i 
    return suma 
    if amigos(n) == m and amigos(m) == n: 
        print( 'los numeros %d y %d son amigos' %(n,m)  )
   
if __name__=="__main__":
    n=int(input("Ingrese x: "))
    m=int(input("Ingrese y: "))
    