def findpeak(a,row,col,mid):
    max1 = 0
    maxindex = findmax(a,row,mid,max1)
    if(mid ==0 or mid==col-1):
        return max1
    if(max1 >=a[maxindex][mid-1] and max1>=a[maxindex][mid+1]):
        return max1
    if(max1<a[maxindex][mid-1]):
        return findpeak(a,row,col,mid-mid/2);
    return findpeak(a,row,col,mid+mid/2)
def find
       
        
