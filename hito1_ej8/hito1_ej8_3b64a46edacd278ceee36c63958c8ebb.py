#Descomponer un número
a = int(input("Ingrese numero de hasta cuatro digitos"))
aM = a//1000
aC = a//100 - aM*10
aD = a//10 - aC*10 -aM*100
aU = a%10
print(aM,"M +",aC,"C +",aD,"D +",aU,"U") 