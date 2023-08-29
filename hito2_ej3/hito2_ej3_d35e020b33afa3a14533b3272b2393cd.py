subsecuencia=input()
n=int(input())
largo=len(subsecuencia)
if largo%n==0:
    miau=largo//n
    secuencia1=subsecuencia[0:miau]
    print(subsecuencia)
else:
    print("ninguna")
    