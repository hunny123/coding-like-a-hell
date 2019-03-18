def counting(a,l,r):
    if(l<=r):
        mid = (l+r)//2
        if(a[mid]!=a[mid-1] and a[mid]!=a[mid+1]):
            return a[mid]
        if(a[mid+1]==a[mid]):
            if(mid%2==0):
                return counting(a,l,mid-1)
            else:
                return counting(a,mid+1,r)
        if(a[mid-1]==a[mid]):
            if(mid%2==0):
                return counting(a,mid+1,r)
            else:
                return counting(a,l,mid-1)
             
                
a=[-1,1,1,2,2,3,3,4,4,5,-1]
l=0
print(counting(a,l,len(a)-1))
            
