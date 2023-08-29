#Subsecuencias de ADN

secuencia=input("Secuencia: ")

secuencia=secuencia.upper()

n=int(input("Número de caracteres de substring: "))

substring=[]

if n<len(secuencia):
    i=0
    a=i+n
    while a<len(secuencia):
        a=i+n
        substring.append(secuencia[i:a])
        i=i+1
    i=0
    a=i+n
    x=True
    while a<len(secuencia):
        a=i+n
        if substring.count(secuencia[i:a])<2:
            print(secuencia[i:a])
            x=False
            substring.append(secuencia[i:a])
        i=i+1
    if x==True:
        print("ninguna")