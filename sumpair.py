a,x = [2,2,3,3,3,4,4],6
i,j = 0,len(a)-1
while(i<j ):
    if(a[i]+a[j]<x):
        i=i+1
    elif(a[i]+a[j]>x):
        j=j-1

    else:
        print((a[i],a[j]))
        temp =j
        while i<temp-1 and a[temp]==a[temp-1]:
            temp = temp-1
            print((i,temp))
        i=i+1    
