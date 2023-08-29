def alineamiento(s1,s2):
    let=""
    for i in s1:
        for k in s2:
            if i == k:
                let += k
            else:
                let += '_'
    return let
