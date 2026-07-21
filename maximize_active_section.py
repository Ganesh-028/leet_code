class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')
        ans = ones

        t = "1" + s + "1"
        n = len(t)

        blocks = []
        i = 0

        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            blocks.append((t[i], j - i))
            i = j

        for i in range(1, len(blocks) - 1):
            if (
                blocks[i][0] == '1'
                and blocks[i - 1][0] == '0'
                and blocks[i + 1][0] == '0'
            ):
                lost = blocks[i][1]
                gained = blocks[i - 1][1] + lost + blocks[i + 1][1]
                ans = max(ans, ones - lost + gained)

        return ans
