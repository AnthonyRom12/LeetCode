"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
""" 


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i: int = 0
        j: int = len(height) - 1
        answer: int = 0
        while i != j:
            answer = max(answer, (j - i) * min(height[i], height[j]))
            
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return answer

obj = Solution()
print(obj.maxArea)
