# 3
def med(str1,str2):
    len1,len2 = len(str1),len(str2)
    dp = [[0] * (len2+1) for _ in range(len1+1)]
    for i in range(len1+1):
        dp[i][0] = i
    for j in range(len2+1):
        dp[0][j] = j
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
    return dp[len1][len2]

test_cases = [
    ("kitten", "sitting"),
    ("flaw", "lawn"),
    ("intention", "execution"),
    ("horse", "ros"),
    ("", "abc"),
    ("abc", "abc"),
    ("abcd", "abcd"),
    ("kitten", "kitten"),
]

for str1,str2 in test_cases:
    meeee = med(str1,str2)
    print(f"min edit distance between ('{str1}' and '{str2}') : {meeee}")
