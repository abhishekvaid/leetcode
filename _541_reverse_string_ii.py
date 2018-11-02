class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        l = list(s)
        i = 0
        while i < len(s):
            j = min(i + k - 1, len(s) - 1)
            for offset in range((j-i+1) //2):
                l[i+offset], l[j-offset] = l[j-offset], l[i+offset]
            i = j + k + 1
        return "".join(l)


assert Solution().reverseStr("abcdefg", 2) == "bacdfeg"