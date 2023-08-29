#Descomponer un número

num = int(input("Ingrese Un Numero de 4 cifras:"))
mil = (num-(num%1000))/1000
res = num%1000
cen = (res-(res%100))//100
res = num%100
dec = (res-(res%10))//10
uni = res%10
print("Milesima : ",int (mil))
print("Centena : ", int (cen))
print("Decena: ", int (dec))
print("Unidad : ", int (uni))