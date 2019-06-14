from collections import Counter


# class Solution:
#     def threeSum(self, nums):
#         total_list=[]
#         k=[]
#         for i,a in enumerate(nums):
#             for j,b in enumerate(nums[i+1]):
#                 for k,c in enumerate(nums[i+j+2:]):
#                     if a+b+c==0 and Counter([a,b,c]) not in k:
#                         k.append(Counter([a,b,c]))
#         for i in k:
#             total_list.append(list(i.elements()))
#         return total_list

class Solution:
    def threeSum(self,nums):
        nums_hash={}
        result=list()
        for num in nums:
            nums_hash[num]=nums_hash.get(num,0)+1
        if 0 in nums_hash and nums_hash[0] >=3:
            result.append([0,0,0])

        neg=list(filter(lambda x:x<0,nums_hash))
        pos=list(filter(lambda x:x>=0,nums_hash))

        for i in neg:
            for j in pos:
                dif=0-i-j
                if dif in nums_hash:
                    if dif in (i,j) and nums_hash[dif]>=2:
                        result.append([i,j,dif])
                    if dif <i or dif>j:
                        result.append([i,j,dif])
        return result

if __name__ == '__main__':
    print(Solution().threeSum([3,4,-7]))