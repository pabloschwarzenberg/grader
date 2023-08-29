n = int(input())
x = 1
def primo(x,n):
    d = 1
    for i in range(x+1,n+1):
        for a in range(2,x+1):
            if i % a == 0:
                d = 0
        if d == 1:
            x = i
            return x
        d = 1    
while n != 1:
    x = primo(x,n)
    if n % x == 0:
        n = int(n/x)
        print(x)
        while n % x == 0:
            n = int(n/x)
            print(x)