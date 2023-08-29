a=eval(input())
b=eval(input())
c=eval(input())
if a >= b >= c:
    print(int(c),",",int(b),",",int(a))
elif a >= c >= b:
    print(int(b),",",int(c),",",int(a))
elif b >= a >= c:
    print(int(c),",",int(a),",",int(b))
elif b >= c >= a:
    print(int(a),",",int(c),",",int(b))
elif c >= a >= b:
    print(int(b),",",int(a),",",int(c))
elif c >= b >= a:
    print(int(a),",",int(b),",",int(c))