def suma_divisores(num):
    res=[i for i in range(1,num-1) if num%i==0]
    if sum(res) !=1:
        return sum(res),(False)
    else:
        return (sum(res)),(True)
           