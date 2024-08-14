class SummaryRanges:
    def __init__(self):
        pass

    def summary_ranges(self, nums):
        result = []
        i = 0
        
        while i < len(nums):
            start = nums[i]  # Start of a sequence
            
            # Continue while the next number is consecutive
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
                
            end = nums[i]  # End of a sequence
            
            # Add the sequence to the result, either as a single number or a range
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}->{end}")
            
            i += 1  # Move to the next number
        
        return result

# Example usage:
if __name__ == "__main__":
    sr = SummaryRanges()
    nums = [0, 1, 2, 4, 5, 7]  # Example input
    print(sr.summary_ranges(nums))  # Output: ['0->2', '4->5', '7']
