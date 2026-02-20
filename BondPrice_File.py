#bondprice

def getBondPrice(y, face, couponRate, m, ppy=2):
  
    n = int(m * ppy)
    rate = y / ppy
    coupon = face * couponRate / ppy

    price = 0
    
    for t in range(1, n+1):
        if t == n:
            cf = coupon + face
        else:
            cf = coupon

        pv = cf / (1 + rate) ** t
        price = price + pv
        
    return(price)