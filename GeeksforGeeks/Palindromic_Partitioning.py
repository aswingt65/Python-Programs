from collections import Counter
class Solution:
    def palindromicPartition(self, s):
        l = []
        for i in range(1,len(s)+1):
            j = 0
            while(j<len(s)):
                if(j+i<len(s)):
                    x = s[j:j+i]
                    c = x[::-1]
                    if(c == s[j:j+i]):
                        l.append(s[j:j+i])
                    j += 1
                elif(j != len(s)):
                    x = s[j:len(s)]
                    c = x[::-1]
                    if(c == s[j:len(s)]):
                        l.append(s[j:len(s)])
                    j = len(s)
                    
        c = 0
        x = s
        for i in reversed(range(len(l))):
            if(l[i] in x):
                x = x.replace(l[i],"#")
                cnt = Counter(x)
                c += cnt["#"]
                if cnt["|"] == len(s):
                    break
                x = x.replace("#","|")
        return c - 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        string = input()
        
        ob = Solution()
        print(ob.palindromicPartition(string))
# } Driver Code Ends
