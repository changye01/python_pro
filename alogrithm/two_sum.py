class Solution:
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 1 break
        # for x in nums:
        #     print(x)

        # 2 break
        # for i in range(len(nums)):
        #     flag = nums[i]
        #     print(flag)x
        #     nums.pop(0)

        # 3
        # success
        # dict = {}
        # for i in range(len(nums)):
        #     if nums[i] in dict:
        #         return [dict[nums[i]], i]
        #     else:
        #         dict[target-nums[i]] = i

        # 4 暴力
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == target-nums[j]:
                    return [i, j]


nums = [2, 7, 11, 15]
so = Solution()
s = so.two_sum(nums, 9)
print(s)
