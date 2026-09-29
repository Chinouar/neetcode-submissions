class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        right = len(matrix) - 1
        left = 0
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] <= target and (mid + 1 >= len(matrix) or matrix[mid + 1][0] > target):
                m = matrix[mid]
                print(m)
                right = len(m) - 1
                left = 0
                while left <= right:
                    mid = (left + right) // 2
                    if m[mid] == target:
                        return True
                    if m[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False
            if matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False