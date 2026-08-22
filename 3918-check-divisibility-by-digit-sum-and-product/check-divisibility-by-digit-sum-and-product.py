class Solution:
    def checkDivisibility(self, n):
        digit_sum = 0
        digit_product = 1
        
        for digit in str(n):
            d = int(digit)
            digit_sum += d
            digit_product *= d
            
        combined_sum = digit_sum + digit_product
        
        return n % combined_sum == 0

