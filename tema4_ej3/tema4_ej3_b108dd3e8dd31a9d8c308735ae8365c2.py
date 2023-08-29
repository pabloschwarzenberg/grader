#def jerigonzo(string):
def jerigonzo(x):
    global vocal
    vocal=('a','e','i','o','u')
    w=('')
    for i in x:
        #print(i)
        w+=i
        for j in vocal:
            if i==j:
                w+='p'+j
           
    return w
   
    