class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in numSet:
            if i - 1 not in numSet:
                next_num = i + 1
                length = 1
                while next_num in numSet:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
        return longest

        # the i-1 is no beautiful, then the next_num in numset
