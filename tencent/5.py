class Solution:
    def longestCommonPrefix(self, strs) -> str:
        common=""
        for i in range(len(strs)):
            for j in range(len(strs[i])):
                for k in range(i+1,len(strs)):
                    if j<len(strs[i]) and strs[i][j]==strs[k][j]:
                        common+=strs[i][j]
                    else:
                        break
                break
            break
        return common


