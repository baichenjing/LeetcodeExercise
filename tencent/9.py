class Solution:
    def removeDuplicates(self,nums):
        if len(nums)<0:
            return 0
        i=0
        j=1
        while j<len(nums):
            if nums[j]!=nums[i]:
                i=i+1
                nums[i]=nums[j]
            j=j+1

        return i+1

if __name__ == '__main__':
    print(Solution().removeDuplicates([]))



