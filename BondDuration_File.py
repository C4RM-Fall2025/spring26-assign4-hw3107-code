

def getBondDuration(y, face, couponRate, m, ppy = 1):
    n = int(m * ppy)
    rate = y / ppy
    coupon = face * couponRate / ppy

    price = 0
    weighted = 0

    for t in range(1, n+1):
        if t == n:
            cashflow = coupon + face
        else:
            cashflow = coupon

        pv = cashflow / (1+rate)**t

        price = price + pv
        weighted = weighted + t * pv

    duration = weighted / price
    x = duration / ppy
    
    return(x)
