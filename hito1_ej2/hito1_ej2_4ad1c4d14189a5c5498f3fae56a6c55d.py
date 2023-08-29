#Contestador de celular

n = int(input())
hour = int(input())
n_1 = str(n)

if (len(n_1) == 8):
    if (hour >= 0) and (hour <= 23):
        if hour <= 7:
            print('CONTESTAR')
        elif hour < 14:         #el elif define todo
            if n%1000 == 909:  
                print('CONTESTAR')
            else:
                print('NO CONTESTAR')
        elif hour >= 17 and hour <= 19:
            if n//100000 == 877:
                print('NO CONTESTAR')
            else:
                print('CONTESTAR')
        elif hour > 19:
            print('NO CONTESTAR')
            
    else:
        False
else:
    False
      