def gcdExt(a, b):
    if(b>a): 
        a, b = b, a
    x0, x1 = 0, 1
    y0, y1 = 1, 0
    while b!= 0:
        x0, x1 = x1, x0 - a//b*x1
        y0, y1 = y1, y0 - a//b*y1 
        a, b = b, a - a//b * b 
    return abs(a), x0, y0
