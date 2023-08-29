num = int(input('.'))

ndigits = len(str(num))

if ndigits == 4:
    digit1 = num//1000
    digit2 = num//100%10
    digit3 = num//10%10
    digit4 = num//1%10

    print(digit1,'M +', digit2,'C +',digit3,'D +',digit4,'U')
elif ndigits == 3:
    digit1 = num//100
    digit2 = num//10%10
    digit3 = num//1%10

    print(digit1,'C +', digit2,'D +',digit3,'U')
elif ndigits == 2:
    digit1 = num//10
    digit2 = num//1%10

    print(digit1,'D +', digit2,'U')
elif ndigits == 1:
    digit1 = num

    print(digit1,'U')
      