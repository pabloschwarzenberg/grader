
divisores_numero = []
def numero_perfecto(a):
    for i in range(1, a):
        if a%i == 0:          
            divisores_numero.append(i)
            
    if sum(divisores_numero) == a:
        return True
    else:
        return False
    

def main():
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
if __name__=="__main__":
    main()