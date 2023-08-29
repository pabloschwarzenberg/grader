def jerigonzo(R):
    Z = []
    for A in R:
        for Q in A:
            if Q in "aeiouAEIOU":
                Q = Q + "p"+ Q
            Z.append(Q)
    Z = "".join(Z)
    return Z
         