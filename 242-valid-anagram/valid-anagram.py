class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashMap={}

        for i in t:
            if i in hashMap:
                hashMap[i]=hashMap[i]+1
            else:
                hashMap[i]=1
        
        for i in s:
            if i in hashMap:
                hashMap[i]=hashMap[i]-1
            else:
                return False
        for i in hashMap:
            if hashMap[i]!=0:
                return False 
        
        return True

