#Descomponer un número
n=int(input("coloque un numero para sacar las unidades "))
mls=(n//1000)
cnt=(n//100%10)
dcm=(n//10%10)
und=(n%10)
print(mls, "m+", cnt, "c+",  dcm, "d+",  und, "u+")