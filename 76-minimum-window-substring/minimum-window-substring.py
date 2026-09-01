class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_hash={}
        for ch in t:
            t_hash[ch] = t_hash.get(ch,0)+1
        req = len(t_hash)
        s_hash = {}
        fmd = 0
        l=0
        ml = float("inf")
        ms = 0
        for r in range(len(s)):
            ch = s[r]
            s_hash[ch] = s_hash.get(ch,0)+1
            if ch in t_hash and s_hash[ch] == t_hash[ch]:
                fmd +=1
            while fmd == req:
                if r-l+1<ml:
                    ml = r-l+1
                    ms = l
                l_ch = s[l]
                s_hash[l_ch] -= 1
                if l_ch in t_hash and s_hash[l_ch]<t_hash[l_ch]:
                    fmd -= 1
                l+= 1
        if ml == float("inf"):
            return ""
        return s[ms:ms+ml]