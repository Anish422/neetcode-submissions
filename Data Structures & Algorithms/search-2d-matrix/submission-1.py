class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0,len(matrix)-1
        while l < r:
            m = l + (r - l) // 2
            if target > matrix[m][-1]:
                l = m+1
            elif target < matrix[m][-1]:
                r = m
            else:
                return True
        
        if not target in set(matrix[l]): return False
        else:
            return True

