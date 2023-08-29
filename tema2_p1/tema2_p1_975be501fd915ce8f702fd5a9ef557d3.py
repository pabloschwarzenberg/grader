# por favor escribe aquí tu función
def es_primo(numero):
    divisores=[]
    cuenta=0
    for i in range(1,numero+1):
        if numero%i==0:
            cuenta=cuenta+1
            divisores.append(i)
    for i in divisores:
        if len(divisores)==2:
            if i*numero== numero:
                num=True
            if i//numero==1:
                num=True
        else:
            num=False
            
    return num
#numero = int(input("Ingrese un número entero positivo: "))           
#Numero= es_primo(numero)

