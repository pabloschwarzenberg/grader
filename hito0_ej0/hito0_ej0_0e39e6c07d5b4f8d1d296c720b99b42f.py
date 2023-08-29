def interpretar(expresion):
    if expresion.isnumeric():
        return int(expresion)

    if '+' in expresion:
        num = 0
        exp = expresion.split('+')
        # print('+', exp)
        for i in exp:
            num += interpretar(i)
        # print(num)
        return num

    if '-' in expresion:
        num = 0
        exp = expresion.split('-')
        # print('-', exp)
        for i in exp:
            num -= interpretar(i)
        # print(num)
        return num

    if '*' in expresion:
        num = 1
        exp = expresion.split('*')
        # print('*', exp)
        for i in exp:
            num *= interpretar(i)
        # print(num)
        return num

    if '/' in expresion:
        exp = expresion.split('/')
        num = interpretar(exp.pop(0))
        # print('/', exp)
        for i in exp:
            num /= interpretar(i)
        # print(num)
        return num

    return 0


resultado = interpretar("2*3+5+6*7/9")
print(resultado)
# el resultado debiera ser 15.66666
