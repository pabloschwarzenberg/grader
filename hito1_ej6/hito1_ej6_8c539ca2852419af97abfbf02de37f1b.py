dates=(input('Ingresa tres numeros, separados por un espacio : '))
arr= dates.split(" ")

def orderSend(arr):
    a=int(arr[0])
    b=int(arr[1])
    c=int(arr[2])
    #1 2 3 
    if a>b:
        if b>c:
            #a>b>c
            print(str(c)+','+str(b)+','+str(a))
        else:
            if c>a:
                 #c>a>b
                print(str(b)+','+str(a)+','+str(c))
            else:
                #a>b
                #c>b
                #a>c
                #a>c>b
                print(str(ab)+','+str(c)+','+str(a))
    else:
        if c>b:
            #b>a
            #c>b
            #a>c
            #b>a>c
            if a>c:
                print(str(c)+','+str(a)+','+str(b))
            else:
                #b>a
                #c>b
                #c>a
                #c>b>a
                 print(str(a)+','+str(b)+','+str(c))
        else:
            #b>a
            #b>c
            #a>c
            #b>a>c
            if a>c:
                print(str(c)+','+str(a)+','+str(b))
            else:
                #b>a
                #b>c
                #c>a
                #b>c>a
                print(str(a)+','+str(c)+','+str(b))

orderSend(arr)