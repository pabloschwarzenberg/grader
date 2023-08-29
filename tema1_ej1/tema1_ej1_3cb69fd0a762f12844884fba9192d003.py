#Suma de los N primeros números
def nprimo(numero):

a = int (input ('input a:'))
 b = int (input ('input b:'))
sum = 0
 
for i in rangen(n + 1)/2:
    k = 2
    if i >= 2:
        while i % k != 0:
            k +=1
        if i==k:
            sum += i
 
print(sum)    