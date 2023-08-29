def es_primo(num, n=2):
    if num == 1:
        return False
    if n >= num:
        print("Es primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        return False