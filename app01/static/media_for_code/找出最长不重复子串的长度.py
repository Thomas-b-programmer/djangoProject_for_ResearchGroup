def lengthOfLongestSubstring(s):
    st = {}
    i, ans = 0, 0  #ans来放字串的长度，i用来存放上一个重复字母的位置
    for j in range(len(s)):
        if s[j] in st:
            i = max(st[s[j]], i) #保证i是最新遍历到重复字母的位置
        ans = max(ans, j - i + 1) #保证ans是最大的，j-i+1是当前遍历到的不重复字串的长度
        st[s[j]] = j + 1  #记下位置
        print(f"j = {j}时候，i = {i},ans = {ans}，j-i+1 = {j-i+1},st = {st}")
    return ans
lengthOfLongestSubstring("ababcdedd")