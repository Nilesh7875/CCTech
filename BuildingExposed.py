def buildings_exposed(x,y,building):
    surface=0
    prev_h=0
    building.sort()
    for i in building:
        h=i[0][1]-i[1][1]
        w=i[2][0]-i[1][0]
        surface=surface+h+w
        if h<prev_h:
            prev_h=prev_h-h
            surface=surface-h-w
        else:
            surface=surface-(prev_h)
            prev_h=h
    return surface
building=[]
n=int(input())
for i in range(n):
    a=[]
    for j in range(4):
        b=[]
        b.append(float(input()))
        b.append(float(input()))
        a.append(b)
    building.append(a)
x=float(input())
y=float(input())
print(buildings_exposed(x,y,building))
