#Edit distance  
#Given two strings s and t. Return the minimum number of operations required to convert s to t.
#example: Input: s = "ycce", t = "ycsce"
#output=1
#explanation: One operation is required inserting 's' between two 'e's of s.

class Solution:
    def editDistance(self, s, t):
        m = len(s)
        n = len(t)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

                else:
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],     # Insert
                        dp[i - 1][j],     # Delete
                        dp[i - 1][j - 1]  # Replace
                    )

        return dp[m][n]


# Example
s = "ycce"
t = "ycsce"

obj = Solution()
print(obj.editDistance(s, t))


#Logic
# if len(s)>len(t):
#     output=len(s)-len(t)
# elif len(t)>len(s):
#     output=len(t)-len(s)
# elif len(s)==len(t):
#     for in range(len(s)):
#         if s[i]!=t[i]:
#             count=count=1
#             output=count
#         print(output)