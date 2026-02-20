#bondprice z 

def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    price = 0

    n = len(times)

    for i in range(n):
        t = times[i]
        r = yc[i]

        if i == n - 1:
            cf = coupon + face
        else:
            cf = coupon

        pv = cf / (1 + r) ** t
        price = price + pv
    
    return(price)