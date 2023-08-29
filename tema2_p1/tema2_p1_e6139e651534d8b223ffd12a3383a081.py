def es_primo(num, n=2):
    if num ==1:
        return False
    elif n >= num:
        print("Es primo")
        return True
    elif num ==1:
        return False
    
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        print("No es primo", n, "es divisor")
        return False