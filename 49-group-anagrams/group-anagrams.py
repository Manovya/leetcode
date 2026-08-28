class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap={}
        for string in strs:
            sort_string = "".join(sorted(string))
            if sort_string in hashMap:
                hashMap[sort_string].append(string)
            else:
                hashMap[sort_string] = [string]
        return list(hashMap.values())