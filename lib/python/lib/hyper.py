def hyper(m, n, r) :
    """Do the hyper level calculation.
hyper(m, 1, r) -> m + r
hyper(m, 2, r) -> m * r
hyper(m, 3, r) -> m ** r"""
    
    if not isinstance(n, int) :
        raise TypeError("argument 2 must be int, not "+str(type(n)).split("'")[1])
    if n <= 0 :
        raise ValueError("argument 2 must be a positive")
    if n == 1 :
        return m + r
    elif n == 2 :
        return m * r
    elif n == 3 :
        return m ** r
    else :
        res = 1
        for i in range(r) :
            res = hyper(m, n-1, res)
        return res
