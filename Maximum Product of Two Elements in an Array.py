class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best_two = [(0, 0), (0, 0)]  # best_two is (val, pos)

        for i, num in enumerate(nums):
            dist_first = num - best_two[0][0]
            dist_second = num - best_two[1][0]

            if dist_first < 0 and dist_second < 0:
                continue
            else:
                best_two = [best_two[0], (num, i)] if dist_second > dist_first else [(num, i), best_two[1]]

        return (best_two[0][0] - 1) * (best_two[1][0] - 1)
