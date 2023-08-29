# por favor escribe aquí tu función

def suma_div(n):
    return sum(k for k in range(1,n+1) if n%k==0)
            
def primos(w):
     print([k for k in range(1,w+1) if suma_div(k)==k+1])
           