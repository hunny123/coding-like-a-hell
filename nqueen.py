
dirx=[1,0,-1,0,1,1,-1,-1]
diry = [0,1,0,-1,1,-1,-1,1]
def verfication(m,i,j,n):
    flag=0
    global dirx,diry
    k=0
    while k<8:
        x,y=i,j
        
            
        while (x>=0 and x<n and y>=0 and y<n):
            if(m[x][y]==1):
                return False
            x=x+dirx[k]
            y=y+diry[k]
        k=k+1
    
    return True
def nqueen(m,q):
    
    
    if q==0:
        return True
    for i in range(n):
        for j in range(n):
           
            if(verfication(m,i,j,n)):    
                m[i][j]=1
                if nqueen(m,q-1):
                    return True
                
                m[i][j]=0
                    
    return False               
                    
n = 4
m = [[0 for x in range(n)] for x in range(n)]


print(nqueen(m,n))
            
