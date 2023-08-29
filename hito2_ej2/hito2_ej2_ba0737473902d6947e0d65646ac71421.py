secuencia=list((input("")).upper())

def validar_secuencia(x):
    y=list("ACTG")
    count=0
    for i in range(0, len(x)):
        for j in range(0,len(y)):
            if x[i]== y[j]:
                count=count+1
    if count==len(x):
        print("secuencia correcta")
    else:
        print("secuencia incorrecta")

validar_secuencia(secuencia)