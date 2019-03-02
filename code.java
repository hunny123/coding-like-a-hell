import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    ArrayList<Integer> sieveOfEratosthenes(int n) 
    { 
       ArrayList<Integer> li = new ArrayList<Integer>();
        boolean prime[] = new boolean[n+1]; 
        for(int i=0;i<n;i++) 
            prime[i] = true; 
          
        for(int p = 2; p*p <=n; p++) 
        { 
            // If prime[p] is not changed, then it is a prime 
            if(prime[p] == true) 
            { 
                // Update all multiples of p 
                for(int i = p*2; i <= n; i += p) 
                    prime[i] = false; 
            } 
        } 
          
        // Print all prime numbers 
        for(int i = 2; i <= n; i++) 
        { 
            if(prime[i] == true) 
               li.add(i); 
        } 
        return (li);
    }
    Integer checker(ArrayList<Integer> li,int a,int b){
        int f=0;
        for(int x=0;x<li.size();x++){
            if(li.get(x) >= a && li.get(x) <= b){
                f++;
            }
        }
        return (f);
    } 




    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        
        Solution g = new Solution(); 
        ArrayList<Integer> lit = g.sieveOfEratosthenes(100000); 
        int n = sc.nextInt();
        ArrayList<Integer>li = new ArrayList<Integer>();
        li.add(0);
        for(int i=1;i<=n;i++){
            li.add(sc.nextInt());
        }
        ArrayList<Integer> fi = new ArrayList<Integer>();
         ArrayList<String> range = new ArrayList<String>(); 
        int q = sc.nextInt();
        for(int i=0;i<q;i++){
            int l = sc.nextInt();
            int u = sc.nextInt();
         
          fi.add(g.checker(lit,li.get(l),li.get(u)));
          String str = Integer.toString(l)+" "+Integer.toString(u);
          range.add(str);
             
        }
        
        int max=Collections.max(fi);
        for(int i=0;i<q;i++){
            if(fi.get(i)==max){
                System.out.print(range.get(i));
                break;
            }
        }
        
        
        
        
       
       
    }
}

