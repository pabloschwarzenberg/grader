vocs=['a','e','i','o','u']
Dictjer={}
for k in vocs:
    Dictjer[k]='p'+k

def jerigonzo(string):
    striping=''
    for i in string:
        striping+=i
        if i in vocs:
            striping+=Dictjer[i]
        string=striping
    return string

if __name__ == "__main__":
    parola=input("Ingrese palabra a traducir: ")
    print("Eso en jerigonzo es {}".format(jerigonzo(parola)))
         