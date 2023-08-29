def amigos(i, j):
    iter = 1
    li = []
    while iter < i:
        res = i % iter
        if res == 0:
            li.append(iter)
        iter += 1

    if len(li) > 0:
        if sum(li) == j:
            return True
        else:
            return False
    else:
        while iter < j:
            res = j % iter
            if res == 0:
                li.append(iter)
            iter += 1
    if len(li) > 0:
        if sum(li) == j:
            return True
        else:
            return False
