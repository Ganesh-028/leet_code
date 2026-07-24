from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX = 2048

        freq = [0] * MAX
        for x in nums:
            freq[x] = 1

        def fwht(a, inv=False):
            n = len(a)
            step = 1
            while step < n:
                jump = step * 2
                for i in range(0, n, jump):
                    for j in range(step):
                        u = a[i + j]
                        v = a[i + j + step]
                        a[i + j] = u + v
                        a[i + j + step] = u - v
                step <<= 1

            if inv:
                for i in range(n):
                    a[i] //= n

        a = freq[:]
        fwht(a)

        for i in range(MAX):
            a[i] = a[i] ** 3

        fwht(a, True)

        ans = 0
        for x in a:
            if x:
                ans += 1

        return ans
