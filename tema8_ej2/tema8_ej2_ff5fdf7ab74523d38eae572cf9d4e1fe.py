def buscarTodas(a,b):
    final=""
    for i in range(0,len(a)):
        if b==a[i]:
            final+=str(i)+" "

    return final[:-1]
    
if __name__ == "__main__":
    pass
           