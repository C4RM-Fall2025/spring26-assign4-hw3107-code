def WhoAmI():
    return('hw3107')



#bondprice E

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


#bondduration

def getBondDuration(y, face, couponRate, m, ppy=1):
    
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


#fizzbuzz

def FizzBuzz(start, finish):
    
    outlist = []

    for i in range (start, finish + 1):

        if i % 3 == 0 and i % 5 == 0:
            outlist.append("fizzbuzz")
        elif i % 3 == 0:
            outlist.append("fizz")
        elif i % 5 == 0:
            outlist.append("buzz")
        else:
            outlist.append(i)
            
    return(outlist)