#Descomponer un número

A = str(int(input()))

if len(A) == 1:

    b = A[0]+"U"

    print(b)

elif len(A) == 2:

    c = A[0]+"D"
    b = A[1]+"U"

    print(c,"+",b)

elif len(A) == 3:

    d = A[0]+"C"
    e = A[1]+"D"
    f = A[2]+"U"

    print(d,"+",e,"+",f)

elif len(A) == 4:

    j = A[0]+"M"
    i = A[1]+"C"
    h = A[2]+"D"
    g = A[3]+"U"

    print(j,"+",i,"+",h,"+",g)
    