numb=int(input("number: "))
def es_primo(numb):
    if numb==2:
         print (2)
    elif numb>1:
        for i in range(2,numb):
            if (numb % i) == 0:
                print(i)
                numb=(numb//i)



    elif numb==1:
         print(1)

es_primo(numb)