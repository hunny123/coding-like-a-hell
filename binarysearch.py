def binarysercg2d(a,l,r,key,rows,cols):
    while (l<=r):
        mid = (l+r)//2
        row = mid/cols
        col = mid%cols
        value = a[row][col]
        if(value ==key):
            return 1
        if(value>key):
            r = mid-1
        else:
            l = mid+1
    return 0            
