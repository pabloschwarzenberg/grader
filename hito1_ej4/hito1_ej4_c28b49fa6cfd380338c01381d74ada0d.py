n=int(input("inserte un numero"))
binario=""
print("tu numero decimal",n)
while n>0:
    residuo=n%2
    n=n//2
    binario=str(residuo)+binario
print("en binario es",binario)

