def setbit(data, x, a):
    if a == 1:
        return data | (1 << x)
    elif a == 0:
        return data & ~(1 << x)
    else:
        raise ValueError("a must be 0 or 1")