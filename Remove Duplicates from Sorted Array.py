class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        first_val = nums[0]
        first_flag = True

        while (nums[0] != first_val) or first_flag:
            first_flag = False

            while nums[0] == nums[1]:
                nums.pop(0)
                if len(nums) == 1:
                    return 1

            val = nums.pop(0)
            nums.append(val)

        return len(nums)