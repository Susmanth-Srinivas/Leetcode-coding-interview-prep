class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle the one overflow edge case per the problem's rules
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values from here on
        dividend, divisor = abs(dividend), abs(divisor)

        result = 0

        # Keep chipping away at dividend until less than divisor remains
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # Double 'temp' as long as it still fits inside dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            # Subtract the biggest chunk that fit, add its count
            dividend -= temp
            result += multiple

        return -result if negative else result