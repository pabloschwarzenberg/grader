def buscarTodas(a,b):
    i=0
    A=list(a)
    global valores
    valores=""

    while i<(len(A)):
        if A[i]==b:
            if i==(len(A)):
                break
            valores=valores+str(i)+" "
            i=i+1
            continue

        else:
            i=i+1
            continue

    return(valores.strip())

if __name__ == "__main__":
    a=input()
    b=input()
    buscarTodas(a,b)
    print(str(valores))