def combination(l,mid,h):
    ar1 = list()
    ar2 = list()
    for x in range(l,mid+1):
        ar1.append(x)
    for j in range(mid+1,r+1):
        ar2.append(j)    
def inversioncount(l,r):
    if(l>=r):
        return 0
    m = (l+r)//2
    le = inversioncount(l,mid)
    ri = inversioncount(mid+1,r)
    combin = conbination()
    return 
