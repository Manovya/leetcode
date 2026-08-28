class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    found =  -1
                    for k in range(j+1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            found = nums2[k]
                            break
                    result.append(found)
                    break
        return result

                  