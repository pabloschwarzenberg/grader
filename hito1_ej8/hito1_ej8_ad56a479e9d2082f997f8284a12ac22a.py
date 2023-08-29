#Descomponer un número
print("MOSTRAR LA M, C, D Y U")
num = int(input("Ingrese Un Número de 4 Cifras : "))
mill = (num)/1000
cen = (num-(num%100))/100
res = num%100
dec = (res-(res%10))/10
uni = res%10
print ("millar: ", int (mill),("M"))
print ("Centena : ",int (cen), "C")
print ("Decena : ",int (dec), "D")
print ("Unidad : ",int (uni), "U")
