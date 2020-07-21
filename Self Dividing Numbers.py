class Solution:
    def selfDividingNumbers(self, left, right):
        return [i for i in range(left, right+1) if Solution._is_self_dividing(i)]
    
    
    @staticmethod
    def _is_self_dividing(n):
        return all((digit != '0') and (n % int(digit) == 0) for digit in str(n))