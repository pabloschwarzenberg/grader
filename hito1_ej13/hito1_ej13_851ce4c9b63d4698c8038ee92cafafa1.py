def desc(n):
    for i in range(2, n+1):
        while n % i == 0:
            print(i)
            n = n/i

n = int(input())
print(desc(n))
      