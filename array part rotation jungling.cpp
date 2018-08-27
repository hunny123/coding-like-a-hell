#include<stdio.h>

int  gcd(int a,int b){
	if(b==0)
	{
		return a;
	}
	else {
		return gcd(b,a%b);
	}
}
void leftrotation(int a[],int d,int n){
  int i =0 ,temp,j;
  for(i=0;i<gcd(d,n);i++){
  	 temp = a[i];
  	 j = i;
  	 while(1){
  	 	int k =j+d;
		if(k>=n){
			k = k-n;
		}
		if(k==i){
			break;
		}
		a[j]=a[k];
		j=k;    
  	 }
  	 a[j]=temp;
  	
  }	
	
}
int main(){
	int a[] = {1,2,3,4,5,6,7};
	leftrotation(a,2,7);
	for(int i=0;i<7;i++){
		printf("%d",a[i]);
		
	}
}
