class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen = {}
        count = 0
        for i in arr:
            if i not in seen:
                seen[i] = i
            else:
                seen[i] += 1
        for i in arr:
            if i + 1 in seen:
                count += 1
        return count
            
