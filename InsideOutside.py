def point_inside_polygon(x,y,poly):

    n = len(poly)
    inside =False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside
    
poly=[]
n=int(input())
for i in range(n):
    a=[]
    for j in range(2):
        a.append(float(input()))
    poly.append(a)
x=float(input())
y=float(input())
z=point_inside_polygon(x,y,poly)
print(z)
