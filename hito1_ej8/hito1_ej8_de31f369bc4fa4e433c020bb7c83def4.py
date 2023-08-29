n = int(input("infrese un numero: "))

mi = n//1000
un = n%10
de = (n%100)//10
ce = (n%1000)//100
    
print(mi,"M +", ce,"C +", de,"D +", un,"U")
