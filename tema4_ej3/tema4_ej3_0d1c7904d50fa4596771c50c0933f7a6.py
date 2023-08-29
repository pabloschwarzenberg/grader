def jerigonzo(palabra):
    jerigoncio=""
    for c in palabra:
    
       if c=="a" or c=="i" or c=="e" or c=="u" or c=="o":
        jerigoncio=jerigoncio + c+"p"+c
        
       else:
        jerigoncio=jerigoncio+c

    return jerigoncio      