#Factores Primos
numero= int(input("dime un numero: "))
divisor= 2
while numero > 1:
             if numero % divisor==0:
                          print(divisor)
                          numero//= divisor
             else:
                          divisor+=1
     