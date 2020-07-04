class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(
            queryTime >= start_time and queryTime <= end_time for (start_time, end_time) in zip(startTime, endTime))
