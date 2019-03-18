def sumset(a,k):
    l = len(a)
    i,j=0,0
    sum1 =0 
    c=0
    
    while(i<l):
        
        print(sum1)
        if(sum1<k):
            sum1 = sum1 + a[i]
            i=i+1
        if(sum1>k):
            sum1 = sum1 -a[j]
            j=j-1
        if(j==l-1 and i==l-1):
            break
        if(sum1==k):
            c=1
            print(i,j)
            return True
    return  False





a,k = [3,6,2,9,10,3],21
print(sumset(a,k))
    
    
