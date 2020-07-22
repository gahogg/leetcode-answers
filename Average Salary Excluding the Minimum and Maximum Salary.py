class Solution:
    # O(n) runtime, O(1) space
    def average(self, salary):
        min_i = 0
        max_i = 0
        total_salary = 0
        n = len(salary)
        for i in range(n):
            if salary[i] < salary[min_i]:
                min_i = i
            
            if salary[i] > salary[max_i]:
                max_i = i
            
            total_salary += salary[i]
        
        return (total_salary - salary[min_i] - salary[max_i]) / (n-2)