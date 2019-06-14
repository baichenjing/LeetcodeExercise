import sys


class Solution:
    def abs(self,num):
        if num<0:
            return -num
        return num

    def threeSumClosest(self,nums,target):
        nums.sort()
        ans=sys.maxsize
        for i in range(len(nums)):
            start=i+1
            end=len(nums)-1
            while start<end:
                sum=nums[start]+nums[end]+nums[i]
                if self.abs(target-sum)<self.abs(target-ans):
                    ans=sum
                if sum>target:
                    end=end-1
                elif sum<target:
                    start=start+1
                else:
                    return ans
        return ans

if __name__ == '__main__':
    print(Solution().threeSumClosest([-1,2,1,-4],1))
