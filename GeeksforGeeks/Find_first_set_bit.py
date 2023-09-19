class Solution:
    def getFirstSetBit(self,n):
     if n==0: return 0
     pos=1
     
     while n>0:
        if n%2==1: 
             return pos
        n=n//2
        pos+=1
     return pos 


#{ 
 # Driver Code Starts.    
def main():   
    T=int(input())    
    while(T>0):                
        n=int(input())
        ob=Solution()      
        print(ob.getFirstSetBit(n))                
        T-=1
if __name__=="__main__":
    main()
# } Driver Code Ends
