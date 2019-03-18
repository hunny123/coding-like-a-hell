def findgreater(a,l,r,key):
    if(l<=r):
        mid = (l+r)//2
        if(a[mid]==key):
            return a[mid+1]
        if(a[mid]<key and a[mid+1]>key):
            return a[mid+1]
        if(a[mid]>key):
            return findgreater(a,l,mid-1,key)
        if(a[mid]<key):
            return findgreater(a,mid+1,r,key)
a =[1,2,3,4,5,7]
           
print(findgreater(a,0,len(a)-1,5))           
           
