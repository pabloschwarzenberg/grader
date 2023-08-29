#CONDICIONES PRIMO

def es_primo(primo):
    if primo <=1:
        return False
    elif primo == 2 :
        return True
    else:
        for i in range(2, primo):
            if primo % i == 0:
                return False
        return True

