class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapp = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []
        def bt(index,current):
            if index==len(digits):
                res.append(current)
                return
            letters = mapp[digits[index]]
            for letter in letters:
                bt(index+1,current+letter)
        bt(0,"")
        return res
        