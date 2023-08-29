def numero_perfecto(n):
    
    perfect_sum = 0
    
    for i in range(1,n):
        if n%i==0:
            perfect_sum += i
            
    return perfect_sum == n
    

perfecto = True
     
if __name__ == "__main__":      
    number = int(input('Enter number: '))
    numero_perfecto(number)
    if numero_perfecto(number):
        print('%d is PERFECT' %(number))
        print(perfecto)
    else:
        print('%d is NOT PERFECT' %(number))
        print(False)
