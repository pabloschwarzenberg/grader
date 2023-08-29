#Descomponer un número
if __name__ == '__main__':
    print("Ingrese Número de 4 Cifras : ")
    num = int(input())
    mil =(num-(num%1000))/1000
    res1= num%1000
    cen = (res1-(res1%100))/100
    res = res1%100
    dec = (res-(res%10))/10
    uni = res%10
    print(int(mil), "M+", int(cen), "C+", int(dec), "D+", int(uni), "U")
