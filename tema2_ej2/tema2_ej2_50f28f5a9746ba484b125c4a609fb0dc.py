def amigos(a, b):
    def sumadiv(num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum+= i
        return sum
    asum = sumadiv(a)
    bsum = sumadiv(b)
    if asum == b and bsum == a:
        return True
    else:
        return False