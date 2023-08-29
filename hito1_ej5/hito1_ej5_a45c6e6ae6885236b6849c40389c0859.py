def digito(num):
    s=str(num)[::-1]
    values = [2, 3, 4, 5, 6, 7]
    total=sum([int(s[i])*values[i%6] for i in range(len(s))])
    return 11-(total%11)
          print("dv=",return)