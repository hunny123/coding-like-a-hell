count=0
def isplain(s):
    return s[:]==s[::-1]


def partitions(s,l,r):
    global count
    if(l>r):
        count=count+1
        
       
    for i in range(l,r+1):
        if(isplain(s[l:i+1])):
            partitions(s,i+1,r)
            
           
partitions("abab",0,3)
print(count)
            
