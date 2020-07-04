class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        cur_x, cur_y = points[0]
        count = 0

        for (target_x, target_y) in points:
            while (cur_x != target_x) or (cur_y != target_y):
                count += 1
                cur_x += Solution.direction(cur_x, target_x)
                cur_y += Solution.direction(cur_y, target_y)

        return count

    @staticmethod
    def direction(cur, target):
        if cur == target:
            return 0
        elif cur < target:
            return 1
        else:
            return -1