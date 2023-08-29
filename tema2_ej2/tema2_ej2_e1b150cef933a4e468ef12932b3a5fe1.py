def amigos (m,n):
    if m!=n:
         suma = 0
         for i in (range(1, m +1 )):
             if m % i == 0:
                 suma +=i
         suma2 = 0
         for i in range(1,n+1 ):
             if n % i == 0:
                 suma2 +=i
         if suma2-n == m and suma-m ==n:
             return True
    return False