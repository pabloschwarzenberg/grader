def numero_perfecto (a):
    divisor=[]
    if a < 1:
        print("error: numero invalido")
    else:
        for i in range(1, a + 1):
            if a%i==0:
                divisor.append(i)
        suma = 0
        for i in range (0, len(divisor)-1):
            suma = suma+divisor[i]
            i+=1
        if suma == a:
            return True
        else:
            return False



if __name__=="__main__":
    num=int(input("Ingrese digito: "))
    print(numero_perfecto(num))