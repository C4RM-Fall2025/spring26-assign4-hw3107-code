
def getBondPrice_E(face, couponRate, yc):
    
    n = len(yc)
    coupon = face * couponRate
    
    price = 0
    
    for t in range(1, n+1):
        rate = yc[t-1]
        pv_factor = 1 / ((1 + rate) ** t)

        if t == n:
            cf = coupon + face
        else: cf = coupon

        price = price + cf * pv_factor
            
    return(price)
