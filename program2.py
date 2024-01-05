class Solution(object):
    def romanToInt(self, s):
        map = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        n = len(s)
        ans = 0
        for i in range(n):
            if i < n - 1 and map[s[i]] < map[s[i+1]]:
                ans -= map[s[i]]
            else:
                ans += map[s[i]]
        
        return ans