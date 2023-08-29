#Descomponer un número
if __name__== "__main__":
    print("Ingrese numero de 4 cifras: ")
    num = int(input())
    mil = (num-(num%1000))/1000
    cen = (num-(num%100))/100
    res = num % 1000
    dec = (res-(res%10))/10
    uni = res%10
    print("Milesima: ", int(mil))
    print("Centena : ",int (cen))
    print("Decena : ",int (dec))
    print("Unidad : ", int (uni))