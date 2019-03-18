def overlapping(a,l,m,h):
    sm = 0
    left_sum=-10000
    for i in range(m,l-1,-1):
        sm = sm+arr[i]
        if(sm>left_sum):
            left_sum = sm

    sm=0
    right_sum =-10000
    for i in range(m+1,h+1):
        sm = sm + arr[i]
        if(sm>right_sum):
            right_sum = sm
    return left_sum + right_sum
def maxsubArray(arr,l,h):
    if(l==h):
        return a[l]
    m = (l+h)//h

    return max(maxsubArray(array, l, m), 
               maxsubArray(arr, m+1, h), 
               overlapping(arr, l, m, h)) 









    
        
