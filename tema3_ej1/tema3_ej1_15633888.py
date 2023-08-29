# completa el código de la función

def suma_divisores(n):
    div=[]
    for i in range(1,n):
        if n%i==0:
            div.append(i)
    if len(div)==1:
        primo_o_no=True
    else:
        primo_o_no=False
    suma=0
    for i in div:
        suma+=i
    
    return suma,primo_o_no