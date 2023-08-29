l=[]

def generar_binario(digitos, n=None):
    if n == None:
        n = ''

    if len(n)==digitos:
        print(n)
        return 
    for i in range(0,2):
        n=n+str(i)
        generar_binario(digitos, n)
        n=n[:-1]
n=int(input())
generar_binario(n)
    
  



           